#!/usr/bin/env python3.6
# coding: utf-8
#urls.PY
# Created on 2018/1/28
# @author: zhaoyun
"""
description:

"""
from django.conf.urls import url,include
from . import views
app_name = 'polls'   #url的命名空间，方便反解不会混淆

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]