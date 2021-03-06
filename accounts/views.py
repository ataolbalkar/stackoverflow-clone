from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, mixins
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accounts.models import UserProfile
from questions import models
from tags.models import Tag
from accounts.forms import RegistrationForm, SetUserUpForm, ProfileSettingsForm, EmailSettingsForm

from django.db.models import Count
from django.urls import reverse_lazy


# Create your views here.

user = get_user_model()


class Registration(CreateView):
    model = user
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        if request.POST.get('type') == 'check_username':
            username = request.POST.get('data')
            if username in [u.username for u in user.objects.all()]:
                result = 'unavailable'
            else:
                result = 'available'

            return JsonResponse({'result': result}, status=200)

        if request.POST.get('type') == 'check_email':
            email = request.POST.get('data')
            if email in [u.email for u in user.objects.all()]:
                result = 'unavailable'
            else:
                result = 'available'

            return JsonResponse({'result': result}, status=200)
        else:
            return super(Registration, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        username = self.request.POST.get('username')
        password = self.request.POST.get('password1')

        account = authenticate(username=username, password=password)
        login(self.request, account)

        return HttpResponseRedirect(reverse_lazy('setup', args=[self.request.user.pk]))


class SetUserUp(UpdateView):
    model = user
    form_class = SetUserUpForm
    template_name = 'account/set_user_up.html'


class ProfileDetail(DetailView):
    model = UserProfile
    template_name = 'account/profile_detail.html'

    def get_object(self, queryset=None):
        object = super(ProfileDetail, self).get_object()

        object.profile_views += 1
        object.save()

        return object

    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        context['answer_count'] = len(models.Answer.objects.filter(author=self.object))
        context['question_count'] = len(models.Question.objects.filter(author=self.object))

        reached_people = 0
        checked_questions = []

        for question in models.Question.objects.filter(author=self.object).all():
            if question.pk in checked_questions:
                continue

            reached_people = reached_people + question.views
            checked_questions.append(question.pk)

        for question in models.Question.objects.filter(questioncomment__author=self.object):
            if question.pk in checked_questions:
                continue
            reached_people = reached_people + question.views
            checked_questions.append(question.pk)

        for question in models.Question.objects.filter(answer__author=self.object):
            if question.pk in checked_questions:
                continue
            reached_people = reached_people + question.views
            checked_questions.append(question.pk)

        for question in models.Question.objects.filter(answer__answercomment__author=self.object):
            if question.pk in checked_questions:
                continue
            reached_people = reached_people + question.views
            checked_questions.append(question.pk)

        context['reached_people'] = reached_people

        users_question_tags = Tag.objects.filter(question__author=self.object).\
            annotate(posts=Count('question'))
        users_answer_tags = Tag.objects.filter(question__answer__author=self.object).\
            annotate(posts=Count('question__answer'))

        users_tags = list(users_question_tags)

        for answer_tag in users_answer_tags:
            if answer_tag in users_question_tags:
                for tag in users_tags:
                    if tag.name == answer_tag.name:
                        tag.posts += answer_tag.posts
                        break
                continue
            else:
                users_tags.append(answer_tag)

        def sort_tags(tag_to_sort):
            return tag_to_sort.posts

        users_tags.sort(key=sort_tags, reverse=True)
        context['users_tag_count'] = len(users_tags)
        context['top_tags'] = users_tags[:6]

        questions = list(models.Question.objects.filter(author=self.object).order_by('-votes'))
        answers = list(models.Answer.objects.filter(author=self.object).order_by('-votes'))

        context['users_post_count'] = len(questions) + len(answers)
        context['top_questions'] = questions[:10]
        context['top_answers'] = answers[:10]

        posts = answers[:10] + questions[:10]

        posts.sort(
            key=lambda x: x.votes,
            reverse=True
        )
        context['top_posts'] = posts[:10]

        questions_sorted = list(models.Question.objects.filter(author=self.object).order_by('-asked_date'))
        answers_sorted = list(models.Answer.objects.filter(author=self.object).order_by('-answered_date'))

        context['top_questions_sorted'] = questions_sorted[:10]
        context['top_answers_sorted'] = answers_sorted[:10]

        posts_sorted = questions_sorted[:10] + answers_sorted[:10]

        def sort_by_date(obj):
            obj_class = obj.__class__.__name__
            if obj_class == 'Question':
                return obj.asked_date
            elif obj_class == 'Answer':
                return obj.answered_date

        posts_sorted.sort(
            key=sort_by_date,
            reverse=True
        )
        context['top_posts_sorted'] = posts_sorted

        return context


class ProfileSettings(mixins.LoginRequiredMixin, UpdateView):
    model = user
    template_name = 'account/profile_settings.html'
    form_class = ProfileSettingsForm
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user == self.get_object():
            return super(ProfileSettings, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('login'))


class EmailSettings(mixins.LoginRequiredMixin, UpdateView):
    model = user
    template_name = 'account/email_settings.html'
    form_class = EmailSettingsForm
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user == self.get_object():
            return super(EmailSettings, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('login'))


class TagSettings(mixins.LoginRequiredMixin, UpdateView):
    model = user
    template_name = 'account/tag_settings.html'
    fields = ('interested_tags', 'ignored_tags')
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user == self.get_object():
            return super(TagSettings, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('login'))

    def post(self, request, *args, **kwargs):
        this_user = get_object_or_404(user, pk=request.user.pk)

        if request.is_ajax:
            tag = get_object_or_404(Tag, pk=request.POST.get('tag'))

            if request.POST.get('type') == 'watch_tag':
                this_user.interested_tags.add(tag)

                return JsonResponse({'tag_url': tag.get_absolute_url()}, status=200)

            elif request.POST.get('type') == 'unwatch_tag':
                this_user.interested_tags.remove(tag)

                return JsonResponse({'status': 'success'}, status=200)

            elif request.POST.get('type') == 'ignore_tag':
                this_user.ignored_tags.add(tag)

                return JsonResponse({'tag_url': tag.get_absolute_url()}, status=200)

            elif request.POST.get('type') == 'unignore_tag':
                this_user.ignored_tags.remove(tag)

                return JsonResponse({'status': 'success'}, status=200)


class DeleteAccount(mixins.LoginRequiredMixin, DeleteView):
    model = user
    template_name = 'account/delete_account.html'
    success_url = '/'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user == self.get_object():
            return super(DeleteAccount, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('login'))

