# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_entry_idtags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AlterField(
            model_name='entry',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='idCategory',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='page.Category'),
        ),
    ]
