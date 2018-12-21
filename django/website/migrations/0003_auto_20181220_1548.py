# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-12-20 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_user_salt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='salt',
        ),
        migrations.AlterField(
            model_name='competition',
            name='competitor_list',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='competition',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='competition',
            name='end_time',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='competition',
            name='jury_list',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='competition',
            name='stage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='competition',
            name='start_time',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='competition',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
