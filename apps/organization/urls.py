from django.conf.urls import url,include
from apps.organization.views import OrgList,UserAskView,DetailHomepageView,DetailTeacherView,DetailCourseView,DetailDescView

urlpatterns = [
    url(r'^list/$', OrgList.as_view(),name='org-list'),
    url(r'^add_ask$',UserAskView.as_view(),name='add_ask'),
    url(r'^detail_homepage',DetailHomepageView.as_view(),name='org_detail_homepage'),
    url(r'^detail_teacher',DetailTeacherView.as_view(),name='org_detail_teachers'),
    url(r'^detail_desc', DetailDescView.as_view(), name='org_detail_desc'),
    url(r'^detail_course', DetailCourseView.as_view(), name='org_detail_course'),
]