# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-03-09 10:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('is_best_answer', models.BooleanField(default=False)),
                ('body', models.TextField(null=True)),
                ('answered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answered_author', to=settings.AUTH_USER_MODEL)),
                ('edited_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answered_edited_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=500)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Answer')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answered_comment_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(null=True)),
                ('votes', models.IntegerField(default=0)),
                ('answers', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('asked_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_modified', models.BooleanField(default=False)),
                ('modified_date', models.DateTimeField(default=None, null=True)),
                ('has_best_answer', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_author', to=settings.AUTH_USER_MODEL)),
                ('modified_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edited_author', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=555)),
                ('votes', models.IntegerField(default=0)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question'),
        ),
    ]
