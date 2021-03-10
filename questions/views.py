from django.shortcuts import render
from questions.models import Question
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView

from django.contrib.auth import get_user_model

from questions.forms import QuestionForm


# Create your views here.

User = get_user_model()

def baseView(request):
    return render(request, 'questions/base_without_sidebar.html')


class QuestionsListView(ListView):
    model = Question
    template_name = 'questions/questions_list.html'

    def get_queryset(self):
        return Question.objects.filter(asked_date__lte=timezone.now()).order_by('asked_date')[:50]


class AskQuestionView(CreateView):
    template_name = 'questions/ask.html'
    form_class = QuestionForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'questions/question_detail.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['modified_author'] = self.object.modified_author
        context['author'] = self.object.author
        return context

    def get_object(self, queryset=None):
        object = super().get_object()
        object.views += 1
        object.save()

        return object

    # def get_context_data(self, **kwargs):
    #     context = super(QuestionDetailView, self).get_context_data(**kwargs)
    #     context['form'] = AnswerForm
    #     return context


# class AnswerQuestionView(FormView):
#     form_class = AnswerForm
#     success_url = ''
