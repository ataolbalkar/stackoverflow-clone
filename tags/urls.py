from django.conf.urls import url

from tags.views import (TagCreateView, TagsListView, TagDetailView, TagsListViewOrderName, TagsListViewOrderNew,
                        TagDetailViewOrderFrequent, TagDetailViewOrderUnanswered, TagDetailViewOrderActive,
                        TagDetailViewOrderBountied, TagDetailViewOrderVotes)


urlpatterns = [
    url(r'^create$', TagCreateView.as_view(), name='create_tag'),
    url(r'^$', TagsListView.as_view(), name='tags_list'),
    url(r'^order=name/$', TagsListViewOrderName.as_view(), name='tag_list_ordered_by_name'),
    url(r'^order=new/$', TagsListViewOrderNew.as_view(), name='tag_list_ordered_by_date'),

    url(r'^(?P<pk>[\w\.\-\+\#]+)/$', TagDetailView.as_view(),
        name='tag_detail'),
    url(r'^(?P<pk>[\w\.\-\+\#]+)/order=active/$', TagDetailViewOrderActive.as_view(),
        name='tag_detail_order_active'),
    url(r'^(?P<pk>[\w\.\-\+\#]+)/order=bountied/$', TagDetailViewOrderBountied.as_view(),
        name='tag_detail_order_bountied'),
    url(r'^(?P<pk>[\w\.\-\+\#]+)/order=unanswered/$', TagDetailViewOrderUnanswered.as_view(),
        name='tag_detail_order_unanswered'),
    url(r'^(?P<pk>[\w\.\-\+\#]+)/order=frequent/$', TagDetailViewOrderFrequent.as_view(),
        name='tag_detail_order_frequent'),
    url(r'^(?P<pk>[\w\.\-\+\#]+)/order=votes/$', TagDetailViewOrderVotes.as_view(),
        name='tag_detail_order_votes')
]
