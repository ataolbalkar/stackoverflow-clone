from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth import get_user_model, mixins
from django.urls import reverse_lazy
from .tasks import send_email_task

import json
import requests


# Create your views here.

User = get_user_model()


class Weather(mixins.LoginRequiredMixin, TemplateView):
    template_name = 'weather/weather.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        print(User.objects.all()[0].email)
        user = self.request.user
        location = user.location
        context = super(Weather, self).get_context_data(**kwargs)

        response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&mode=json&units'
                                f'=metric&cnt=4&appid=2ef36034b02fcd512b4663e91317d470')
        response_now = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&mode=json&units'
                                    f'=metric&cnt=4&appid=2ef36034b02fcd512b4663e91317d470')

        weather_info = json.loads(response.content)
        weather_info_now = json.loads(response_now.content)

        context['weather_now'] = weather_info_now
        context['weather'] = weather_info

        return context
