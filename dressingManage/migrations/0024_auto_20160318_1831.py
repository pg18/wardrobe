# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressingManage', '0023_auto_20160318_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='generating',
            field=models.NullBooleanField(),
        ),
    ]
