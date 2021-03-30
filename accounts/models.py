from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.urls import reverse_lazy


# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self, username, email, password):
        email = self.normalize_email(email)

        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)

    location = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    website = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    full_name = models.CharField(max_length=255, blank=True, null=True)

    reputation = models.IntegerField(default=0)
    profile_views = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    interested_tags = models.ManyToManyField('tags.Tag', blank=True, related_name='interested_tags')
    ignored_tags = models.ManyToManyField('tags.Tag', blank=True, related_name='ignored_tags')

    followed_questions = models.ManyToManyField('questions.Question', blank=True, related_name='followed_questions')
    followed_answers = models.ManyToManyField('questions.Answer', blank=True, related_name='followed_answers')

    voted_questions = models.ManyToManyField('questions.Question', blank=True, related_name='voted_questions')
    voted_down_questions = models.ManyToManyField('questions.Question', blank=True, related_name='voted_down_questions')

    voted_answers = models.ManyToManyField('questions.Answer', blank=True, related_name='voted_answers')
    voted_down_answers = models.ManyToManyField('questions.Answer', blank=True, related_name='voted_down_answers')

    voted_question_comments = models.ManyToManyField('questions.QuestionComment', blank=True, related_name='voted_question_comments')
    voted_down_question_comments = models.ManyToManyField('questions.QuestionComment', blank=True, related_name='voted_down_question_comments')

    voted_answer_comments = models.ManyToManyField('questions.AnswerComment', blank=True, related_name='voted_answer_comments')
    voted_down_answer_comments = models.ManyToManyField('questions.AnswerComment', blank=True, related_name='voted_down_answer_comments')

    registered_date = models.DateTimeField(default=timezone.now)

    object = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def get_absolute_url(self):
        return reverse_lazy('profile_detail', args=[self.pk])

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username
