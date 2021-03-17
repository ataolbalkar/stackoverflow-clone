# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-03-12 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_is_active'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followed_answers',
            field=models.ManyToManyField(blank=True, related_name='followed_answers', to='questions.Answer'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followed_questions',
            field=models.ManyToManyField(blank=True, related_name='followed_questions', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voted_answer_comments',
            field=models.ManyToManyField(blank=True, related_name='voted_answer_comments', to='questions.AnswerComment'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voted_answers',
            field=models.ManyToManyField(blank=True, related_name='voted_answers', to='questions.Answer'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voted_question_comments',
            field=models.ManyToManyField(blank=True, related_name='voted_question_comments', to='questions.QuestionComment'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='voted_questions',
            field=models.ManyToManyField(blank=True, related_name='voted_questions', to='questions.Question'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interested_tags',
            field=models.ManyToManyField(blank=True, related_name='interested_tags', to='tags.Tag'),
        ),
    ]