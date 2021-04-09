from django import forms
from questions.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body', 'tags')


class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')


class AnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('body',)
