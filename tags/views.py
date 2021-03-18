from django.shortcuts import render
from tags.models import Tag
from tags.forms import CreateTagForm
from django.db.models import Count

from django.views.generic import ListView, CreateView


# Create your views here.

class TagCreateView(CreateView):
    model = Tag
    form_class = CreateTagForm
    template_name = 'tags/tag_create.html'
    success_url = '/tags/create'

    def get_context_data(self, **kwargs):
        context = super(TagCreateView, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.annotate(num_questions=Count('question')).order_by('num_questions')

        return context


class TagsListView(ListView):
    model = Tag
    template_name = 'tags/tags_list.html'

