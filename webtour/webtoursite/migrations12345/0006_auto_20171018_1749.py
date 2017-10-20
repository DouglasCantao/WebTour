# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoursite', '0005_auto_20171015_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passageiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(default='00000000000', max_length=11)),
                ('nome', models.CharField(default='Pedroso', max_length=20)),
                ('telefone', models.CharField(default='31995811098', max_length=13)),
                ('email', models.CharField(default='jurassic@viagens.com.br', max_length=50)),
                ('passagem_paga', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='onibus',
            name='autonomia',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=4),
        ),
        migrations.AlterField(
            model_name='onibus',
            name='categoria',
            field=models.CharField(default='Ônibus', max_length=1),
        ),
        migrations.AlterField(
            model_name='onibus',
            name='placa',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='onibus',
            name='qtde_lugares',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='onibus',
            name='veic_pronto',
            field=models.BooleanField(default=True),
        ),
    ]
