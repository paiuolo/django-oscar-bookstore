# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 21:46
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('catalogue', '0008_auto_20160119_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.Author', verbose_name='authors'),
        ),
        migrations.AddField(
            model_name='product',
            name='background_color',
            field=models.CharField(blank=True, max_length=7, verbose_name='background color'),
        ),
        migrations.AddField(
            model_name='product',
            name='bookstores',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.BookStore', verbose_name='bookstores'),
        ),
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/home/pai/hg/oscar-bookstore/source/django-oscar-bookstore/magazzino_virtuale'), upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.BookFormat', verbose_name='format'),
        ),
        migrations.AddField(
            model_name='product',
            name='has_offers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='number_of_pages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='publication_date',
            field=models.DateField(blank=True, null=True, verbose_name='publication date'),
        ),
        migrations.AddField(
            model_name='product',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.Serie', verbose_name='serie'),
        ),
        migrations.AddField(
            model_name='product',
            name='translation_authors',
            field=models.ManyToManyField(blank=True, related_name='books_translated', to='books.Author', verbose_name='translation authors'),
        ),
    ]