# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressingManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='code',
            field=models.CharField(default='#000000', max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
