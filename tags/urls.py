from django.conf.urls import url

from tags.views import TagCreateView


urlpatterns = [
    url(r'^create$', TagCreateView.as_view(), name='create_tag'),
]
