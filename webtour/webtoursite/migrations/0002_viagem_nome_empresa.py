# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoursite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='nome_empresa',
            field=models.CharField(default='Cometex', max_length=25),
            preserve_default=False,
        ),
    ]
