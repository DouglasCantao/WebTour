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