# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-08 08:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateField(db_index=True, default=datetime.datetime(2019, 12, 8, 11, 50, 30, 121187), verbose_name='Опубликована')),
            ],
            options={
                'verbose_name': 'Статья блога',
                'verbose_name_plural': 'Статьи блога',
                'db_table': 'Posts',
                'ordering': ['posted'],
            },
        ),
    ]
