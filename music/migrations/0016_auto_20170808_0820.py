# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0015_auto_20170806_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
    ]