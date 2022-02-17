# coding=utf-8
import json

from django.core import serializers
from django.http import HttpResponse
import random
from Blog.models import Author, Article, Tag

author_name_list = ['bond', 'Fiona', 'Leon', 'ivy', 'Bella']
article_title_list = ['Python 教程', 'Java教程', 'Vue教程']


# Create your views here.
def first_def(request):
    authors = Author.objects.all()
    return response_success(message='请求成功', data_list=serializers.serialize("json", authors))


def created(request):
    data_dict = {'name': 'stephen', 'qq': '1920098158', 'addr': '珠海', 'email': '1920098158@qq.com'}
    author = Author(**data_dict)
    author.save()
    return HttpResponse('success')


def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        # 随机生成9位数的QQ，
        author.qq = ''.join(
            str(random.choice(range(10))) for _ in range(9)
        )
        author.addr = 'addr_%s' % (random.randrange(1, 3))
        author.email = '%s@qq.com' % (author.qq)
        author.save()


def create_articles_and_tags():
    # 随机生成文章
    for article_title in article_title_list:
        # 从文章标题中得到 tag
        tag_name = article_title.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)

        random_author = random.choice(Author.objects.all())

        for i in range(1, 21):
            title = '%s_%s' % (article_title, i)
            article, created = Article.objects.get_or_create(
                title=title, defaults={
                    'author': random_author,  # 随机分配作者
                    'content': '%s 正文' % title,
                    'score': random.randrange(70, 101),  # 随机给文章一个打分
                }
            )
            article.tags.add(tag)


def save_info(request):
    create_authors()
    create_articles_and_tags()
    return response_success('success', True)


def query_info_test(request):
    arts = Article.objects.all().prefetch_related('tags')[:3]
    for art in arts:
        print(art.title, art.tags.all())
    data_list = serializers.serialize("json", arts)
    return response_success('message', data_list=json.loads(data_list))


def response_success(message, data=None, data_list=None):
    if data_list is None:
        data_list = []
    return HttpResponse(json.dumps({
        'code': 200,  # code由前后端配合指定
        'message': message,  # 提示信息
        'data': data,  # 返回单个对象
        'dataList': data_list  # 返回对象数组
    }, ensure_ascii=False), content_type="application/json,charset=utf-8")
