# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20170914_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(max_length=140),
        ),
    ]
