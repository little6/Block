# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-09 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.IntegerField(default=False, verbose_name='维护人员'),
        ),
    ]
