from django.db import models
from django.contrib.auth.models import User



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
	placa = models.CharField(max_length=7)
	categoria = models.CharField(max_length=1)
	qtde_lugares = models.IntegerField()
	autonomia = models.DecimalField(max_digits=3, decimal_places=2)
	veic_pronto = models.BooleanField()
	onibus_viagem = models.ForeignKey('Viagem')
