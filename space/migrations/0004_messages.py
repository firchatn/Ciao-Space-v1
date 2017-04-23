# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('singup', '0011_auto_20170411_1545'),
        ('space', '0003_remove_post_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=2000)),
                ('msg_date', models.DateTimeField(auto_now_add=True, verbose_name='date cheek')),
                ('fromUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singup.users')),
            ],
        ),
    ]
