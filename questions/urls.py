from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^$', views.QuestionsListView.as_view(), name='question_list'),
    url(r'^ask/$', views.AskQuestionView.as_view(), name='ask'),
    url(r'^question/(?P<pk>\d+)$', views.QuestionDetailView.as_view(), name='question_detail'),
    url(r'^question/(?P<pk>\d+)/sort=oldest$',
        views.QuestionDetailViewSortOldest.as_view(),
        name='question_detail_sort_oldest'),
    url(r'^question/(?P<pk>\d+)/sort=active$',
        views.QuestionDetailViewSortActive.as_view(),
        name='question_detail_sort_active'),
]
