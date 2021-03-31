from django.conf.urls import url

from accounts.views import ProfileDetail, ProfileSettings, EmailSettings, TagSettings


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileDetail.as_view(), name='profile_detail'),
    url(r'^(?P<pk>\d+)/profile-settings/$', ProfileSettings.as_view(), name='profile_settings'),
    url(r'^(?P<pk>\d+)/email-settings/$', EmailSettings.as_view(), name='email_settings'),
    url(r'^(?P<pk>\d+)/tag-settings/$', TagSettings.as_view(), name='tag_settings'),
]
