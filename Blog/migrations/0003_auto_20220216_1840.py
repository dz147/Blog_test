# Generated by Django 2.2 on 2022-02-16 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20220216_1830'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='blog_article',
        ),
        migrations.AlterModelTable(
            name='author',
            table='blog_author',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='blog_tag',
        ),
    ]
