from django.conf.urls import url

from accounts.views import ProfileDetail


urlpatterns = [
    url(r'^(?P<pk>\d+)', ProfileDetail.as_view(), name='profile_detail'),
]
