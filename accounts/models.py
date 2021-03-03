from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


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
    password = models.CharField(max_length=255, blank=False, null=False)

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

    registered_date = models.DateTimeField(default=timezone.now)

    object = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username
