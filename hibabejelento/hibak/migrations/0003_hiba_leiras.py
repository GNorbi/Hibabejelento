# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-10 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hibak', '0002_hiba_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiba',
            name='leiras',
            field=models.TextField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]