from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^$', views.QuestionsListView.as_view(), name='question_list'),
    url(r'^\?order=hot$', views.QuestionListViewOrderHot.as_view(), name='question_list_hot'),
    url(r'^\?order=week$', views.QuestionListViewOrderWeek.as_view(), name='question_list_week'),
    url(r'^\?order=month$', views.QuestionListViewOrderMonth.as_view(), name='question_list_month'),

    url(r'^ask/$', views.AskQuestionView.as_view(), name='ask'),

    url(r'^question/(?P<pk>\d+)/$', views.QuestionDetailView.as_view(), name='question_detail'),
    url(r'^question/(?P<pk>\d+)?sort=oldest/$',
        views.QuestionDetailViewSortOldest.as_view(),
        name='question_detail_sort_oldest'),
    url(r'^question/(?P<pk>\d+)?sort=active/$',
        views.QuestionDetailViewSortActive.as_view(),
        name='question_detail_sort_active'),

    url(r'^question/(?P<pk>\d+)/update$', views.QuestionUpdateView.as_view(), name='question_update'),
    url(r'^answer/(?P<pk>\d+)/update$', views.AnswerUpdateView.as_view(), name='answer_update'),
]
