# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-08 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainshow',
            name='productid1',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='mainshow',
            name='productid2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='mainshow',
            name='productid3',
            field=models.CharField(default='', max_length=10),
        ),
    ]