from django.conf.urls import url

from tags.views import TagCreateView, TagsListView, TagDetailView


urlpatterns = [
    url(r'^create$', TagCreateView.as_view(), name='create_tag'),
    url(r'^$', TagsListView.as_view(), name='tags_list'),
    url(r'^profile/(?P<name>[\w.@+-]+)$', TagDetailView.as_view(), name='tag_detail')
]
