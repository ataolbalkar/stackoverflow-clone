from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^$', views.QuestionsListView.as_view(), name='question_list'),
    url(r'^ask/$', views.AskQuestionView.as_view(), name='ask'),
]
