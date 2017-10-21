# Python
from decimal import Decimal

# Django
from django.db import models
from django.contrib.auth.models import User

#Classes em Python que representam as tabelas do banco de dados
#A princípio as tabelas não estão normalizadas. Serão atualizadas em uma oportunidade próxima.
class Viagem(models.Model):
	nome_empresa = models.CharField(max_length=25)
	origem = models.CharField(max_length=250)
	destino = models.CharField(max_length=250)
	data_saida = models.CharField(max_length=250)
	data_chegada = models.CharField(max_length=250)
	hora_saida = models.CharField(max_length=250)
	hora_chegada = models.CharField(max_length=250)
	qtde_assentos = models.CharField(max_length=50)
	qtde_assentos_disp = models.CharField(max_length=50)


class Onibus(models.Model):
	placa = models.CharField(max_length=7, default='')
	categoria = models.CharField(max_length=1, default=u'Ônibus')
	qtde_lugares = models.IntegerField(default=0)
	autonomia = models.DecimalField(max_digits=4, decimal_places=2, default='0.00')
	veic_pronto = models.BooleanField(default=True)


class Passageiro(models.Model):
	cpf = models.CharField(max_length=11, default='00000000000')
	nome = models.CharField(max_length=20, default='Pedroso')
	telefone = models.CharField(max_length=13, default='31995811098')
	email = models.CharField(max_length=50, default='jurassic@viagens.com.br')