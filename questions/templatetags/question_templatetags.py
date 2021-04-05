from django import template
from django.urls import reverse_lazy

register = template.Library()


website_link = 'localhost:1234'


@register.filter
def get_model_name(obj):
    return obj.__class__.__name__


@register.filter
def get_question_link(pk):
    return website_link + str(reverse_lazy('question_detail', args=[pk]))


@register.filter
def get_answer_link(question_pk, answer_pk):
    return website_link + str(reverse_lazy('question_detail', args=[question_pk])) + 'answer-content--' + answer_pk
