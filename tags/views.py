from django.shortcuts import render

from tags.models import Tag
from questions.models import Question

from tags.forms import CreateTagForm
from django.db.models import Count

from django.http import JsonResponse

from django.core import serializers
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder

from django.views.generic import ListView, CreateView, DetailView


# Create your views here.

class TagCreateView(CreateView):
    model = Tag
    form_class = CreateTagForm
    template_name = 'tags/tag_create.html'
    success_url = '/tags/create'

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

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context['question_list'] = Question.objects.filter(tags__name__iexact=self.object.name).order_by('-asked_date')

        return context
