# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-05 06:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='城市')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
            ],
            options={
                'verbose_name_plural': '城市',
                'verbose_name': '城市',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', models.TextField(verbose_name='机构描述')),
                ('click_num', models.IntegerField(verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('address', models.CharField(max_length=150, verbose_name='机构地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDict', verbose_name='所在城市')),
            ],
            options={
                'verbose_name_plural': '机构',
                'verbose_name': '机构',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='教师名')),
                ('work_years', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=50, verbose_name='就职公司')),
                ('work_position', models.CharField(max_length=50, verbose_name='公司职位')),
                ('point', models.CharField(max_length=50, verbose_name='教学特点')),
                ('click_num', models.IntegerField(verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='教学机构')),
            ],
            options={
                'verbose_name_plural': '教师信息',
                'verbose_name': '教师信息',
            },
        ),
    ]
