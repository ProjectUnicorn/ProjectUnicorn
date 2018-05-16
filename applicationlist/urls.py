# -*- encoding: utf-8 -*-
from django.conf.urls import url
from django.http import HttpResponseRedirect
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as authviews
from . import views

urlpatterns = [
    url(r'^$', views.ApplicationListTableView.as_view(), name='applicationlist_index'),
    url(r'^api/applicationlist/', views.ApplicationList.as_view()),
    url(r'^api/application/(?P<applicationId>\d+)/$', views.ApplicationDetail.as_view()),
    url(r'^api/token/', authviews.obtain_auth_token),
    url(r'^edit/(?P<applicationId>\d+)/$', views.Edit, name='applicationlist_edit'),
    url(r'^accounts/profile/', views.ApplicationListTableView.as_view(), name='applicationlist_index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
