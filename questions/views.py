from django.shortcuts import render
from questions.models import Question
from django.utils import timezone
from django.views.generic import ListView


# Create your views here.

def baseView(request):
    return render(request, 'questions/base.html')


class QuestionsListView(ListView):
    model = Question
    template_name = 'questions/questions_list.html'

    def get_queryset(self):
        return Question.objects.filter(asked_date__lte=timezone.now()).order_by('asked_date')[:50]
