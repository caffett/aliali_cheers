# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-27 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpages', '0009_auto_20161124_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.ImageField(null=True, upload_to='videos/cover/'),
        ),
    ]