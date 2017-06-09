# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interviewTest', '0006_clientaccount_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_address', models.CharField(max_length=20)),
                ('place_of_birth', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='interviewTest.ClientAccount')),
            ],
        ),
    ]
