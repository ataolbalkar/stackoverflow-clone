from django.db import models
from tags.models import Tag
from django.utils import timezone
from django.contrib.auth import get_user_model


UserProfile = get_user_model()
# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    author = models.ForeignKey(UserProfile, related_name='question_author')

    votes = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag, blank=True)
    asked_date = models.DateTimeField(default=timezone.now)

    is_modified = models.BooleanField(default=False)
    modified_date = models.DateTimeField(default=None, null=True)
    modified_author = models.ForeignKey(UserProfile, related_name='edited_author', null=True)

    has_best_answer = models.BooleanField(default=False)


class QuestionComment(models.Model):
    question = models.ForeignKey(Question)
    author = models.ForeignKey(UserProfile, related_name='comment_author')
    comment = models.CharField(max_length=555)

    votes = models.IntegerField(default=0)

    posted_date = models.DateTimeField(default=timezone.now)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    author = models.ForeignKey(UserProfile, related_name='answered_author')
    votes = models.IntegerField(default=0)
    is_best_answer = models.BooleanField(default=False)

    body = models.TextField(null=True)

    answered_date = models.DateTimeField(default=timezone.now)
    edited_author = models.ForeignKey(UserProfile, related_name='answered_edited_author', null=True)
    edited_date = models.DateTimeField(default=timezone.now, null=True)


class AnswerComment(models.Model):
    answer = models.ForeignKey(Answer)
    author = models.ForeignKey(UserProfile, related_name='answered_comment_author')
    votes = models.IntegerField(default=0)

    comment = models.CharField(max_length=500)

    posted_date = models.DateTimeField(default=timezone.now)
