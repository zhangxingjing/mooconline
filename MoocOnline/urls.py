"""MoocOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from MoocOnline import settings
from apps.users.views import LoginView,RegisterView,TeacherList,CourseList
from apps.organization.views import OrgList
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^org/',include('apps.organization.urls')),
    url(r'^teacher-list/$',TeacherList.as_view(),name='teachers-list'),
    url(r'^course-list/$',CourseList.as_view(),name='course-list'),
    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATICFILES_DIRS,'show_indexes':True}),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,'show_indexes':True}),

]