# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-03-12 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_is_active'),
        ('accounts', '0003_auto_20210312_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='voted_down_answer_comments',
            field=models.ManyToManyField(blank=True, related_name='voted_down_answer_comments', to='questions.AnswerComment'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voted_down_answers',
            field=models.ManyToManyField(blank=True, related_name='voted_down_answers', to='questions.Answer'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voted_down_question_comments',
            field=models.ManyToManyField(blank=True, related_name='voted_down_question_comments', to='questions.QuestionComment'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voted_down_questions',
            field=models.ManyToManyField(blank=True, related_name='voted_down_questions', to='questions.Question'),
        ),
    ]
