# encoding: utf-8
# Author    : Davide<1920098158@qq.com>
# Datetime  : 2022/2/18 14:47
# User      : Stephen
# Product   : PyCharm
# Project   : Blog_test
# File      : MyController.py
# explain   : 文件说明
from django.http import HttpRequest, HttpResponse
from django.views import View


class MyView(View):
    def get(self, request):
        return HttpResponse('success')

    def post(self, request, *args, **kwargs):
        print(request)
        return HttpResponse('success - post')

    def get_info(self, request, *args, **kwargs):
        print(request)
        return HttpResponse('success - name')
