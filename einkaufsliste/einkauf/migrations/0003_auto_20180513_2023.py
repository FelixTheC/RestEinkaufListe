# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-13 20:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('einkauf', '0002_auto_20180426_1858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 13, 20, 23, 26, 155724), editable=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 13, 20, 23, 26, 155066), editable=False),
        ),
    ]
