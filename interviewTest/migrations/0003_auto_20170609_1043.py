# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviewTest', '0002_auto_20170609_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientaccount',
            name='created_on',
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='DOB',
            field=models.DateField(null=True),
        ),
    ]
