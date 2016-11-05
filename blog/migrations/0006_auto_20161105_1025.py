# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161105_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default=None, null=True, unique=True),
        ),
    ]