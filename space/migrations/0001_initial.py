# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DecimalField(decimal_places=16, max_digits=20)),
                ('y', models.DecimalField(decimal_places=16, max_digits=20)),
                ('cheek_date', models.DateTimeField(auto_now_add=True, verbose_name='date cheek')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromUser', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=2000)),
                ('msg_date', models.DateTimeField(auto_now_add=True, verbose_name='date cheek')),
                ('toUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('aboutnow', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
