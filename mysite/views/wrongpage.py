#!/usr/bin/env python3.6
# coding: utf-8
#wrongpage.PY
# Created on 2018/1/29
# @author: zhaoyun
"""
description:

"""
from django.shortcuts import get_object_or_404, render, redirect
from   django.http import Http404
from  django.http import HttpResponse,HttpResponseNotFound
from polls.models import Choice,Question

def my_custom_page_not_found_view(request,foo):
    print(foo)
    return HttpResponseNotFound('就是骚')

def my_custom_page_not_found_view_pro(request,foo):
    print(foo)
    # return render(request,'templates.mysite.notfound.html', {"foo": foo})
    # django.template.loaders.app_directories.Loader: C:\Users\zhaoyun\PycharmProjects
    # \mysite\polls\templates\templates.mysite.otfound.html (Source does not exist)
    return render(request,'notfound.html', {"foo": foo})
# render(request, template_name, context=None, content_type=None, status=None,
#        using=None)


def viewArticles(request, year, month):
    text = "Displaying articles of : %s/%s"%(year, month)
    return HttpResponse(text)


def my_custom_page_not_found_view_two(request,foo):
    # q = Question.objects.all()

    # print(q.question_text,"00000000000000000000000000")
    # return redirect("https://www.baidu.com",permanent=False)
    # return redirect('polls:index')
    return redirect("viewArticles", year = "2045", month = "02")

