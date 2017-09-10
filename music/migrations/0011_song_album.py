# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_remove_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
    ]