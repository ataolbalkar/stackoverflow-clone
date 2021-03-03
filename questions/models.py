from django.db import models
from accounts.models import UserProfile
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    author = models.ForeignKey(UserProfile)
    votes = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    # @TODO tag eklenecek
    asked_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    has_best_answer = models.BooleanField(default=False)


class QuestionComment(models.Model):
    question = models.ForeignKey(Question)
    author = models.ForeignKey(UserProfile)
    comment = models.CharField(max_length=555)

    votes = models.IntegerField(default=0)

    posted_date = models.DateTimeField(default=timezone.now)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    author = models.ForeignKey(UserProfile)
    votes = models.IntegerField(default=0)
    is_best_answer = models.BooleanField(default=False)

    body = models.TextField(null=True)

    answered_date = models.DateTimeField(default=timezone.now)
    # @TODO editleyen author eklenecek.
    edited_date = models.DateTimeField(default=timezone.now)


class AnswerComment(models.Model):
    answer = models.ForeignKey(Answer)
    author = models.ForeignKey(UserProfile)
    votes = models.IntegerField(default=0)

    comment = models.CharField(max_length=500)

    posted_date = models.DateTimeField(default=timezone.now)

