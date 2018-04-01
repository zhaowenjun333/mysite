"""mysite URL Configuration

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
from django.http import HttpResponse, HttpResponseNotFound
from .views.wrongpage import *


def view_badpage(request):
    return HttpResponseNotFound('Not found')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mi/', view_badpage),
    url(r'^getoneyuan/', my_custom_page_not_found_view, {"foo": "bar"}),  # http://127.0.0.1:8000/getoneyuan/
    url(r'^get10000yuan/', my_custom_page_not_found_view_pro, {"foo": "zuomengba"}),
    url(r'^get20000yuan/', my_custom_page_not_found_view_two, {"foo": "lllllll"}),
    url(r'^polls/', include('polls.urls'))  # namespace='polls'
]
# def include(arg, namespace=None, app_name=None):
#  第一个参数是 instance namespace 只能在项目的urls定义
#  第二个参数是 app namespace  （可以在 总urls 和app的urls里面定义）
# 使用方法有两种：1 只在项目URL中写namespace
#               2.只在app的URL中写app_name
#               3.在项目的url中写app_name 和 namespace