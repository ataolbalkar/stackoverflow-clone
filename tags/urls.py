from django.conf.urls import url

from tags.views import TagCreateView, TagsListView, TagDetailView, TagsListViewOrderName, TagsListViewOrderNew


urlpatterns = [
    url(r'^create$', TagCreateView.as_view(), name='create_tag'),
    url(r'^$', TagsListView.as_view(), name='tags_list'),
    url(r'^order=name/$', TagsListViewOrderName.as_view(), name='tag_list_ordered_by_name'),
    url(r'^order=new/$', TagsListViewOrderNew.as_view(), name='tag_list_ordered_by_date'),
    url(r'^(?P<pk>[\w\.\-]+)/$', TagDetailView.as_view(), name='tag_detail')
]
