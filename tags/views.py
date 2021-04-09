from django.shortcuts import render, get_object_or_404

from tags.models import Tag
from questions.models import Question
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from tags.forms import CreateTagForm
from django.db.models import Count

from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.core import serializers

from django.views.generic import ListView, CreateView, DetailView


# Create your views here.

User = get_user_model()


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = CreateTagForm
    template_name = 'tags/tag_create.html'
    success_url = '/tags/create'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_manager:
            return super(TagCreateView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse_lazy('login'))

    def get_context_data(self, **kwargs):
        context = super(TagCreateView, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.annotate(count=Count('question')).order_by('count')

        return context


class TagsListView(ListView):
    model = Tag
    template_name = 'tags/tags_list.html'
    paginate_by = 45
    order_by = 'vote'

    def get_queryset(self):
        return self.model.objects.annotate(count=Count('question')).order_by('-count')

    def get_context_data(self, **kwargs):
        context = super(TagsListView, self).get_context_data(**kwargs)
        context['order_by'] = self.order_by

        return context

    def post(self, request):
        if request.is_ajax:
            value = request.POST.get('value')
            data = self.model.objects.filter(name__icontains=value).\
                annotate(count=Count('question')).order_by('-count')[:45]

            counts = [_.count for _ in data]
            serialized_data = serializers.serialize('json', data)

            return JsonResponse({'data': serialized_data,
                                 'counts': counts},
                                status=200, safe=False)


class TagsListViewOrderName(TagsListView):
    order_by = 'name'

    def get_queryset(self):
        return self.model.objects.annotate(count=Count('question')).order_by('pk')

    def post(self, request):
        if request.is_ajax:
            value = request.POST.get('value')
            data = self.model.objects.filter(name__icontains=value).\
                annotate(count=Count('question')).order_by('pk')[:45]

            counts = [_.count for _ in data]
            serialized_data = serializers.serialize('json', data)

            return JsonResponse({'data': serialized_data,
                                 'counts': counts},
                                status=200, safe=False)


class TagsListViewOrderNew(TagsListView):
    order_by = 'date'

    def get_queryset(self):
        return self.model.objects.annotate(count=Count('question')).order_by('created_date')

    def post(self, request):
        if request.is_ajax:
            value = request.POST.get('value')
            data = self.model.objects.filter(name__icontains=value).\
                annotate(count=Count('question')).order_by('created_date')[:45]

            counts = [_.count for _ in data]
            serialized_data = serializers.serialize('json', data)

            return JsonResponse({'data': serialized_data,
                                 'counts': counts},
                                status=200, safe=False)


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tags/tag_detail.html'
    order_by = 'newest'

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context['order_by'] = self.order_by
        context['question_list'] = Question.objects.filter(tags__name__iexact=self.object.name).\
            annotate(answer_count=Count('answer')).order_by('-asked_date')

        return context

    def post(self, request, pk):
        user = get_object_or_404(User, pk=request.user.pk)
        tag = get_object_or_404(Tag, pk=pk)
        process_type = request.POST.get('type')

        if request.is_ajax:
            if process_type == 'watch_tag':
                if tag in user.ignored_tags.all():
                    user.ignored_tags.remove(tag)

                user.interested_tags.add(tag)

                return JsonResponse(
                    {
                        'data': f"'{pk}', successfully added to '{user.username}'s interested tags.",
                    },
                    status=200
                )

            elif process_type == 'unwatch_tag':
                user.interested_tags.remove(tag)

                return JsonResponse(
                    {
                        'data': f"'{pk}', successfully removed from '{user.username}'s interested tags.",
                    },
                    status=200
                )

            elif process_type == 'ignore_tag':
                if tag in user.interested_tags.all():
                    user.interested_tags.remove(tag)

                user.ignored_tags.add(tag)

                return JsonResponse(
                    {
                        'data': f"'{pk}', successfully added to '{user.username}'s ignored tags.",
                    },
                    status=200
                )

            elif process_type == 'unignore_tag':
                user.ignored_tags.remove(tag)

                return JsonResponse(
                    {
                        'data': f"'{pk}', successfully removed from '{user.username}'s ignored tags.",
                    },
                    status=200
                )


class TagDetailViewOrderActive(TagDetailView):
    order_by = 'active'


class TagDetailViewOrderBountied(TagDetailView):
    order_by = 'bountied'


class TagDetailViewOrderUnanswered(TagDetailView):
    order_by = 'unanswered'

    def get_context_data(self, **kwargs):
        context = super(TagDetailViewOrderUnanswered, self).get_context_data(**kwargs)
        context['order_by'] = self.order_by
        context['question_list'] = Question.objects.filter(tags__name__iexact=self.object.name).\
            annotate(answer_count=Count('answer')).filter(answer_count=0).order_by('-asked_date')

        return context


class TagDetailViewOrderFrequent(TagDetailView):
    order_by = 'frequent'

    def get_context_data(self, **kwargs):
        context = super(TagDetailViewOrderFrequent, self).get_context_data(**kwargs)
        context['order_by'] = self.order_by
        context['question_list'] = Question.objects.filter(tags__name__iexact=self.object.name). \
            annotate(answer_count=Count('answer')).order_by('-views')

        return context


class TagDetailViewOrderVotes(TagDetailView):
    order_by = 'votes'

    def get_context_data(self, **kwargs):
        context = super(TagDetailViewOrderVotes, self).get_context_data(**kwargs)
        context['order_by'] = self.order_by
        context['question_list'] = Question.objects.filter(tags__name__iexact=self.object.name). \
            annotate(answer_count=Count('answer')).order_by('-votes')

        return context
