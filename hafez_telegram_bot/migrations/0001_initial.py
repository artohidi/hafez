# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-07 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hafez_Fall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='شعر')),
                ('description', models.TextField(verbose_name='تفسیر')),
            ],
            options={
                'verbose_name': 'فال حافظ',
                'verbose_name_plural': 'فال حافظ',
            },
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, unique=True, verbose_name='کد کاربری تلگرام')),
                ('username', models.CharField(max_length=100, verbose_name='نام انتخابی کاربر')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام کاربر')),
                ('last_name', models.CharField(max_length=100, verbose_name='فامیل کاربر')),
                ('state', models.CharField(default='صفحه اول', max_length=200, verbose_name='موقعیت در ربات')),
            ],
            options={
                'verbose_name': 'کاربران تلگرام بات',
                'verbose_name_plural': 'کاربران تلگرام بات',
            },
        ),
    ]