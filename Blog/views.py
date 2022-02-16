from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Author


# Create your views here.
def first_def(request):
    return HttpResponse(Author.objects.all())


def created(request):
    data_dict = {'name': 'stephen', 'qq': '1920098158', 'addr': '珠海', 'email': '1920098158@qq.com'}
    author = Author(**data_dict)
    author.save()
    return HttpResponse('success')
