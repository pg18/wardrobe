# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressingManage', '0028_auto_20160318_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outfit',
            name='temp',
        ),
        migrations.AddField(
            model_name='outfit',
            name='ptsCoat',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='outfit',
            name='ptsPant',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='outfit',
            name='ptsShoes',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='outfit',
            name='ptsTop',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='outfit',
            name='ptsVarious',
            field=models.PositiveIntegerField(null=True),
        ),
    ]