# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_auto_20161211_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='fA_bkColor',
            field=models.CharField(max_length=30, verbose_name='FontAwesome Background Color'),
        ),
        migrations.AlterField(
            model_name='social',
            name='fA_brand',
            field=models.CharField(max_length=30, verbose_name='FontAwesome Icon'),
        ),
    ]