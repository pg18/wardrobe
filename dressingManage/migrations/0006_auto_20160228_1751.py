# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressingManage', '0005_auto_20160227_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothe',
            name='quantity1',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothe',
            name='quantity2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clothe',
            name='quantity3',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
