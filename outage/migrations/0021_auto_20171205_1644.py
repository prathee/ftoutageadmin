# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-05 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outage', '0020_auto_20161012_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='died'),
        ),
    ]
