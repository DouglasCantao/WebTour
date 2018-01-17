#-*- coding:utf-8 -*-

# Python
from decimal import Decimal

# Django
from django.db.models import Model, CharField, IntegerField, DecimalField
from django.db.models import BooleanField
from django.contrib.auth.models import User
from django.db import models

# Classes em Python que representam as tabelas do banco de dados
# A princípio as tabelas não estão normalizadas. Serão atualizadas em uma
# oportunidade próxima.
class Viagem(models.Model):
    nome_empresa = models.CharField(max_length=25)
    origem = CharField(max_length=250)
    destino = CharField(max_length=250)
    data_saida = CharField(max_length=250)
    data_chegada = CharField(max_length=250)
    hora_saida = CharField(max_length=250)
    hora_chegada = CharField(max_length=250)
    qtde_assentos = CharField(max_length=50)
    qtde_assentos_disp = CharField(max_length=50)
    dono_id = IntegerField(default=0)


class Onibus(models.Model):
    placa = CharField(max_length=7, default='')
    categoria = CharField(max_length=1, default=u'Ônibus')
    qtde_lugares = IntegerField(default=0)
    autonomia = DecimalField(max_digits=4, decimal_places=2, default='0.00')
    veic_pronto = BooleanField(default=True)
    dono_id = IntegerField(default=0)


class Passageiro(models.Model):
    cpf = CharField(max_length=11, default='')
    nome = CharField(max_length=20, default='')
    telefone = CharField(max_length=13, default='')
    email = CharField(max_length=50, default='')
    dono_id = IntegerField(default=0)


class Motorista(models.Model):
    cnh = models.CharField(max_length=13, default='')
    nome = models.CharField(max_length=25, default='')
    telefone = models.CharField(max_length=16, default='')
    email = models.CharField(max_length=40, default='')
    dono_id = IntegerField(default=0)