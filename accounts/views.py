from django.shortcuts import render
from django.views.generic import DetailView
from accounts.models import UserProfile


# Create your views here.

class ProfileDetail(DetailView):
    model = UserProfile
    template_name = 'account/profile_detail.html'
