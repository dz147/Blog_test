# coding=utf-8
import json

from django.core import serializers
from django.http import HttpResponse

from Blog.models import Author


# Create your views here.
def first_def(request):
    authors = Author.objects.all()
    return response_success(message='请求成功', data_list=serializers.serialize("json", authors))


def created(request):
    data_dict = {'name': 'stephen', 'qq': '1920098158', 'addr': '珠海', 'email': '1920098158@qq.com'}
    author = Author(**data_dict)
    author.save()
    return HttpResponse('success')


def response_success(message, data=None, data_list=None):
    if data_list is None:
        data_list = []
    return HttpResponse(json.dumps({
        'code': 200,  # code由前后端配合指定
        'message': message,  # 提示信息
        'data': data,  # 返回单个对象
        'dataList': data_list  # 返回对象数组
    }), 'application/json')
