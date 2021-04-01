"""stackoverflow_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from questions import views
from accounts.views import Registration, SetUserUp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.QuestionsListView.as_view(), name='index'),
    url(r'^register/$', Registration.as_view(), name='registration'),
    url(r'^(?P<pk>\d+)/setup/$', SetUserUp.as_view(), name='setup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^base/$', views.baseView, name='base'),
    url(r'questions/', include('questions.urls')),
    url(r'tags/', include('tags.urls')),
    url(r'account/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
