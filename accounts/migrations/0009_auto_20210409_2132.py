# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-04-09 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210409_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='stack.png', null=True, upload_to=''),
        ),
    ]
