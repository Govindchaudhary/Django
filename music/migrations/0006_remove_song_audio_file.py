# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 03:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20170803_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='audio_file',
        ),
    ]
