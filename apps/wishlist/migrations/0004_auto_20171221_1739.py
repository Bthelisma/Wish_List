# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0003_wish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='user_wish',
        ),
        migrations.RemoveField(
            model_name='wish',
            name='users',
        ),
        migrations.AddField(
            model_name='wish',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='items_added', to='wishlist.User'),
        ),
        migrations.AddField(
            model_name='wish',
            name='wishlist',
            field=models.ManyToManyField(default='', related_name='wishes', to='wishlist.User'),
        ),
    ]