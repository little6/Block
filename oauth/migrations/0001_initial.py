# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-07 10:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
                ('refresh_token', models.CharField(blank=True, max_length=255, null=True, verbose_name='refresh_token')),
                ('provider', models.IntegerField(choices=[(1, 'Github'), (2, 'QQ'), (3, 'Coding')], max_length=10, verbose_name='类别')),
                ('bound_at', models.DateTimeField(auto_now_add=True, verbose_name='绑定时间')),
                ('expire_at', models.DateTimeField(blank=True, null=True, verbose_name='token失效时间')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='绑定帐户')),
            ],
        ),
    ]
