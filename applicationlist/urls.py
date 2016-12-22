# -*- encoding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ApplicationListTableView.as_view(), name='applicationlist_index'),
]
