from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from webtoursite.models import Viagem

def index(request):
	if request.method == 'POST':
		for key, value in request.POST.items():
			print(key, value)

		return render(request, 'paineldecontrole.html')

	return render(request, 'index.html')



def entrar(request):
	return render(request, 'entrar.html')

def contato(request):
	return render(request, 'contato.html')




def cadastro(request):
	if request.method == 'POST':
		for key, value in request.POST.items():
			print(key, value)

		return render(request, 'index.html')

	return render(request, 'cadastro.html')

def paineldecontrole(request):
	return render(request, 'paineldecontrole.html')

def onibus(request):
	viagens = Viagem.objects.all()

	ctx = {'viagens': viagens}

	return render(request, 'onibus.html', ctx)

def passageiro(request):
	return render(request, 'passageiro.html')