# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-03-20 21:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 21, 55, 39, 57177, tzinfo=utc)),
        ),
    ]