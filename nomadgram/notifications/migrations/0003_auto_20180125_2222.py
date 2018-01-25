# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-25 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20180125_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.Image'),
        ),
    ]
