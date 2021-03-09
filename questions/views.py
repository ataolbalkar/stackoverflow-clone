from django.shortcuts import render
from questions.models import Question
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, TemplateView


from questions.forms import QuestionForm


# Create your views here.


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





# def ask_question(request):
#     if request.method == 'POST':
#         pass
#
#     else:
#         form = QuestionForm
#
#
#         return render(request, 'questions/ask.html', {'form': form})


class QuestionDetailView(DetailView):
    model = Question
