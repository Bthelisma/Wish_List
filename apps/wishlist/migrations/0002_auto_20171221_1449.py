# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.AddField(
            model_name='user',
            name='hireddate',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
