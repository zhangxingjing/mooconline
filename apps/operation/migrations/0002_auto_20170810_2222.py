# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-10 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userask',
            name='mobile',
            field=models.IntegerField(max_length=11, verbose_name='手机'),
        ),
    ]