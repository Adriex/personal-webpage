# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_auto_20161211_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='link',
            field=models.CharField(max_length=2000, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='social',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
    ]
