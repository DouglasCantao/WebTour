# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtoursite', '0003_onibus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onibus',
            name='onibus_viagem',
        ),
    ]
