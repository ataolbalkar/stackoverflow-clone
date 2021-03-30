from django.conf.urls import url

from accounts.views import ProfileDetail, ProfileSettings


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileDetail.as_view(), name='profile_detail'),
    url(r'^(?P<pk>\d+)/profile-settings/$', ProfileSettings.as_view(), name='profile_settings'),
]
