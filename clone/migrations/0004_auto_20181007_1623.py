# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-07 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0003_auto_20181004_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=60),
        ),
    ]
