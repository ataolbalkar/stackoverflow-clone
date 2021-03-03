# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-03-03 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('info', models.TextField(blank=True, null=True)),
                ('related_tags', models.ManyToManyField(blank=True, null=True, related_name='_tag_related_tags_+', to='tags.Tag')),
            ],
        ),
    ]
