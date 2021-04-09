# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.core.mail import send_mail

import requests
import json

from django.contrib.auth import get_user_model
from django.template import Context
from django.template.loader import get_template

user_model = get_user_model()


@shared_task(bind=True,
             name='send_email_task',
             max_retries=3,
             soft_time_limit=20)
def send_email_task(self):
    users = user_model.objects.all()
    template = get_template('weather/weather_email.html')

    for user in users:
        if user.location:
            location = user.location
            response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&mode=json&units'
                                    f'=metric&cnt=4&appid=2ef36034b02fcd512b4663e91317d470')
            response_now = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&mode=json&units'
                                        f'=metric&cnt=4&appid=2ef36034b02fcd512b4663e91317d470')

            weather_info = json.loads(response.content)
            weather_info_now = json.loads(response_now.content)
            context = Context({'weather_now': weather_info_now,
                               'weather': weather_info})
            content = template.render(context.flatten())

            send_mail(subject=f'Hourly Weather Forecast - {location}',
                      html_message= content,
                      message=f'Hourly Weather Forecast - {location}',
                      from_email='galyus.deneme@gmail.com',
                      recipient_list=[user.email])
    return None
