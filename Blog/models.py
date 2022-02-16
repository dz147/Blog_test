from django.db import models


# Create your models here.

# 作者
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()

    class Meta:
        db_table = 'blog_author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 博客
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    tags = models.ManyToManyField('Tag')

    class Meta:
        db_table = 'blog_article'
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'blog_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
