# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-11 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hibak', '0006_auto_20170711_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='alkalmazott',
            name='cim',
            field=models.CharField(default='', help_text='Alkalmazott cime', max_length=200),
        ),
        migrations.AddField(
            model_name='alkalmazott',
            name='telefonszam',
            field=models.CharField(default='+36201234567', help_text='Alkalmazott telefonszama', max_length=200),
        ),
    ]
