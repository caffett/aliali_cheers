# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-02 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpages', '0010_auto_20161127_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_comment',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='picture_comment',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='video_comment',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]