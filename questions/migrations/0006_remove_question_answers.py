# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-03-16 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
    ]
