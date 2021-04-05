from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from questions.models import Question, QuestionComment, Answer, AnswerComment
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView, UpdateView

from questions.forms import QuestionForm, QuestionUpdateForm, AnswerUpdateForm

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Count
from datetime import datetime, timedelta
from django.utils import timezone

from questions.data_processes import find_last_activity

# Create your views here.

User = get_user_model()


class QuestionsListView(ListView):
    model = Question
    template_name = 'questions/questions_list.html'
    order_by = 'interesting'

    def get_queryset(self):
        if self.request.user.is_authenticated():
            user = get_object_or_404(User, pk=self.request.user.pk)
            interested_tags = [tag.name for tag in user.interested_tags.all()]
            ignored_tags = [tag.name for tag in user.ignored_tags.all()]

            if len(interested_tags) > 0:
                first_set = Question.objects.filter(tags__name__in=interested_tags)
            else:
                first_set = Question.objects.all()

            if len(ignored_tags) > 0:
                second_set = Question.objects.exclude(tags__name__in=ignored_tags)
            else:
                second_set = Question.objects.all()

            final_set = first_set | second_set
            return final_set.exclude(tags__name__in=ignored_tags).annotate(answer_count=Count('answer')).order_by(
                'answer_count', '-asked_date')[:100]

        else:
            return Question.objects.annotate(answer_count=Count('answer')) \
                       .order_by('answer_count', '-asked_date')[:100]

    def get_context_data(self, **kwargs):
        context = super(QuestionsListView, self).get_context_data(**kwargs)

        context['order_by'] = self.order_by

        return context


class QuestionListViewOrderHot(QuestionsListView):
    order_by = 'hot'

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.request.user.pk)
        ignored_tags = [tag.name for tag in user.ignored_tags.all()]

        if self.request.user.is_authenticated():
            return Question.objects.exclude(tags__name__in=ignored_tags) \
                       .filter(asked_date__lte=timezone.now()).order_by('-asked_date')[:100]
        else:
            return Question.objects.filter(asked_date__lte=timezone.now()).order_by('-asked_date')[:100]


class QuestionListViewOrderWeek(QuestionsListView):
    order_by = 'week'

    def get_queryset(self):
        this_week = datetime.today() - timedelta(days=7)

        if self.request.user.is_authenticated():
            user = get_object_or_404(User, pk=self.request.user.pk)
            ignored_tags = [tag.name for tag in user.ignored_tags.all()]

            return Question.objects.exclude(tags__name__in=ignored_tags) \
                       .filter(asked_date__gte=this_week).order_by('-views', '-votes')[:100]

        else:
            return Question.objects.filter(asked_date__gte=this_week).order_by('-views', '-votes')[:100]


class QuestionListViewOrderMonth(QuestionsListView):
    order_by = 'month'

    def get_queryset(self):
        this_month = datetime.today() - timedelta(days=30)

        if self.request.user.is_authenticated():
            user = get_object_or_404(User, pk=self.request.user.pk)
            ignored_tags = [tag.name for tag in user.ignored_tags.all()]

            return Question.objects.exclude(tags__name__in=ignored_tags) \
                       .filter(asked_date__gte=this_month).order_by('-views', '-votes')[:100]

        else:
            return Question.objects.filter(asked_date__gte=this_month).order_by('-views', '-votes')[:100]


class AskQuestionView(LoginRequiredMixin, CreateView):
    template_name = 'questions/ask.html'
    login_url = reverse_lazy('login')
    form_class = QuestionForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'questions/question_detail.html'
    sort_type = 'vote'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['modified_author'] = self.object.modified_author
        context['author'] = self.object.author

        question_comments = QuestionComment.objects.filter(question=self.object)
        context['question_comments'] = question_comments.order_by('-votes')

        answers = Answer.objects.filter(question=self.object)

        context['sort_type'] = self.sort_type
        if self.sort_type == 'active':
            context['answers'] = answers.order_by('-answered_date')
        elif self.sort_type == 'date':
            context['answers'] = answers.order_by('answered_date')
        else:
            context['answers'] = answers.order_by('-is_best_answer', '-votes')

        answer_comments = AnswerComment.objects.filter(answer__question=self.object)
        context['answer_comments'] = answer_comments.order_by('-votes')

        activities = [self.object.asked_date]

        try:
            activities.append(self.object.modified_date)
        except AttributeError:
            pass

        try:
            activities.append(question_comments.order_by('-posted_date').first().posted_date)
        except AttributeError:
            pass

        try:
            activities.append(answers.order_by('-answered_date').first().answered_date)
        except AttributeError:
            pass

        try:
            activities.append(answers.order_by('-edited_date').first().edited_date)
        except AttributeError:
            pass

        try:
            activities.append(answer_comments.order_by('-posted_date').first().posted_date)
        except AttributeError:
            pass

        context['last_activity_time'] = find_last_activity(activities)
        return context

    def get_object(self, queryset=None):
        object = super().get_object()
        object.views += 1
        object.save()

        question_author = get_object_or_404(User, pk=object.author.pk)
        question_author.reputation += 0.1
        question_author.save()

        for answer in object.answer_set.all():
            if answer.is_best_answer:
                answer_author = get_object_or_404(User, pk=answer.author.pk)
                answer_author.reputation += 0.1
                answer_author.save()

        return object

    def post(self, request, pk):
        user = get_object_or_404(User, pk=request.user.pk)
        if request.is_ajax():
            if request.POST.get('type') == 'vote_up':
                if request.POST.get('object') == 'question':
                    question = get_object_or_404(Question, pk=pk)
                    question.votes += 1
                    question.save()

                    author = get_object_or_404(User, pk=question.author.pk)
                    author.reputation += 1
                    author.save()

                    if question in user.voted_down_questions.all():
                        user.voted_down_questions.remove(question)

                    if request.POST.get('voted_before') == 'false':
                        user.voted_questions.add(question)

                elif request.POST.get('object') == 'question_comment':
                    question_comment = get_object_or_404(QuestionComment, pk=request.POST.get('pk'))
                    question_comment.votes += 1
                    question_comment.save()

                    author = get_object_or_404(User, pk=question_comment.author.pk)
                    author.reputation += 1
                    author.save()

                    if question_comment in user.voted_down_question_comments.all():
                        user.voted_down_question_comments.remove(question_comment)

                    if request.POST.get('voted_before') == 'false':
                        user.voted_question_comments.add(question_comment)

                elif request.POST.get('object') == 'answer':
                    answer = get_object_or_404(Answer, pk=request.POST.get('pk'))
                    answer.votes += 1
                    answer.save()

                    author = get_object_or_404(User, pk=answer.author.pk)
                    author.reputation += 1
                    author.save()

                    if answer in request.user.voted_down_answers.all():
                        user.voted_down_answers.remove(answer)

                    if request.POST.get('voted_before') == 'false':
                        user.voted_answers.add(answer)

                elif request.POST.get('object') == 'answer_comment':
                    answer_comment = get_object_or_404(AnswerComment, pk=request.POST.get('pk'))
                    answer_comment.votes += 1
                    answer_comment.save()

                    author = get_object_or_404(User, pk=answer_comment.author.pk)
                    author.reputation += 1
                    author.save()

                    if answer_comment in user.voted_down_answer_comments.all():
                        user.voted_down_answer_comments.remove(answer_comment)

                    if request.POST.get('voted_before') == 'false':
                        user.voted_answer_comments.add(answer_comment)

            elif request.POST.get('type') == 'vote_down':
                if request.POST.get('object') == 'question':
                    question = get_object_or_404(Question, pk=pk)
                    question.votes -= 1
                    question.save()

                    author = get_object_or_404(User, pk=question.author.pk)
                    author.reputation -= 1
                    author.save()

                    if question in user.voted_questions.all():
                        user.voted_questions.remove(question)

                    if request.POST.get('voted_before') == 'false':
                        user.voted_down_questions.add(question)

                elif request.POST.get('object') == 'question_comment':
                    question_comment = get_object_or_404(QuestionComment, pk=request.POST.get('pk'))
                    question_comment.votes -= 1
                    question_comment.save()

                    author = get_object_or_404(User, pk=question_comment.author.pk)
                    author.reputation -= 1
                    author.save()

                    if question_comment in user.voted_question_comments.all():
                        user.voted_question_comments.remove(question_comment)

                    if request.POST.get('voted_before') == 'false':
                        user.voted_down_question_comments.add(question_comment)

                elif request.POST.get('object') == 'answer':
                    answer = get_object_or_404(Answer, pk=request.POST.get('pk'))
                    answer.votes -= 1
                    answer.save()

                    author = get_object_or_404(User, pk=answer.author.pk)
                    author.reputation -= 1
                    author.save()

                    if answer in request.user.voted_answers.all():
                        user.voted_answers.remove(answer)

                    if request.POST.get('voted_before') == 'false':
                        user.voted_down_answers.add(answer)

                elif request.POST.get('object') == 'answer_comment':
                    answer_comment = get_object_or_404(AnswerComment, pk=request.POST.get('pk'))
                    answer_comment.votes -= 1
                    answer_comment.save()

                    author = get_object_or_404(User, pk=answer_comment.author.pk)
                    author.reputation -= 1
                    author.save()

                    if answer_comment in user.voted_answer_comments.all():
                        user.voted_answer_comments.remove(answer_comment)

                    if request.POST.get('voted_before') == 'false':
                        user.voted_down_answer_comments.add(answer_comment)

            elif request.POST.get('type') == 'comment':
                if request.POST.get('object') == 'question_comment':
                    comment = QuestionComment(
                        question=get_object_or_404(Question, pk=pk),
                        author=user,
                        comment=request.POST.get('content')
                    )
                    comment.save()

                    return JsonResponse({'user': comment.author.username,
                                         'comment': comment.comment,
                                         'date': 'now'},
                                        status=200)

                if request.POST.get('object') == 'answer_comment':
                    comment = AnswerComment(
                        answer=get_object_or_404(Answer, pk=request.POST.get('pk')),
                        author=user,
                        comment=request.POST.get('content')
                    )
                    comment.save()

                    return JsonResponse({'user': comment.author.username,
                                         'comment': comment.comment,
                                         'date': 'now'},
                                        status=200)

            elif request.POST.get('type') == 'answer':
                answer = Answer(
                    question=get_object_or_404(Question, pk=pk),
                    author=user,
                    body=request.POST.get('content')
                )
                answer.save()

            elif request.POST.get('type') == 'set_best_answer':
                answer = get_object_or_404(Answer, pk=request.POST.get('pk'))
                question = answer.question
                if (not question.has_best_answer) and (not answer.is_best_answer):
                    answer.is_best_answer = True
                    question.has_best_answer = True

                    author = get_object_or_404(User, pk=answer.author.pk)
                    author.reputation += 20
                    author.save()

                    answer.save()
                    question.save()

                    return JsonResponse({'data': 'success'}, status=200)

            elif request.POST.get('type') == 'unset_best_answer':
                answer = get_object_or_404(Answer, pk=request.POST.get('pk'))
                question = answer.question
                if question.has_best_answer and answer.is_best_answer:
                    answer.is_best_answer = False
                    question.has_best_answer = False

                    author = get_object_or_404(User, pk=answer.author.pk)
                    author.reputation -= 20
                    author.save()

                    answer.save()
                    question.save()

                    return JsonResponse({'data': 'success'}, status=200)

        return JsonResponse({'status': 'success'}, status=200)


class QuestionDetailViewSortOldest(QuestionDetailView):
    sort_type = 'date'


class QuestionDetailViewSortActive(QuestionDetailView):
    sort_type = 'active'


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionUpdateForm
    template_name = 'questions/question_update.html'
    login_url = reverse_lazy('login')
    success_url = '.'

    def get(self, request, *args, **kwargs):
        if request.user == self.get_object().author:
            return super(QuestionUpdateView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('login'))

    def post(self, request, *args, **kwargs):
        question = self.get_object()
        question.is_modified = True
        question.modified_date = timezone.now()
        question.modified_author = get_object_or_404(User, pk=request.user.pk)

        question.body = request.POST.get('body')
        question.title = request.POST.get('title')
        question.save()

        return HttpResponseRedirect(self.success_url)


class AnswerUpdateView(LoginRequiredMixin, UpdateView):
    model = Answer
    form_class = AnswerUpdateForm
    template_name = 'questions/answer_update.html'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user == self.get_object().author:
            return super(AnswerUpdateView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('login'))

    def get_context_data(self, **kwargs):
        context = super(AnswerUpdateView, self).get_context_data(**kwargs)
        context['question'] = self.get_object().question

        return context
