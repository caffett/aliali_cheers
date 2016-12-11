# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-02 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Webpages', '0013_auto_20161202_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio_comment',
            name='like',
        ),
        migrations.RemoveField(
            model_name='picture_comment',
            name='like',
        ),
        migrations.RemoveField(
            model_name='video_comment',
            name='like',
        ),
        migrations.AlterField(
            model_name='collect_item',
            name='audio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Collect_Audio', to='Webpages.Audio'),
        ),
        migrations.AlterField(
            model_name='collect_item',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Collect_Picture', to='Webpages.Picture'),
        ),
        migrations.AlterField(
            model_name='collect_item',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Collect_Video', to='Webpages.Video'),
        ),
        migrations.AlterField(
            model_name='dislike_item',
            name='audio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dislike_Audio', to='Webpages.Audio'),
        ),
        migrations.AlterField(
            model_name='dislike_item',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dislike_Picture', to='Webpages.Picture'),
        ),
        migrations.AlterField(
            model_name='dislike_item',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dislike_Video', to='Webpages.Video'),
        ),
        migrations.AlterField(
            model_name='like_item',
            name='audio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Like_Audio', to='Webpages.Audio'),
        ),
        migrations.AlterField(
            model_name='like_item',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Like_Picture', to='Webpages.Picture'),
        ),
        migrations.AlterField(
            model_name='like_item',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Like_Video', to='Webpages.Video'),
        ),
    ]