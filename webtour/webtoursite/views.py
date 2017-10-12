from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from webtoursite.models import Viagem, Onibus
from webtoursite.forms import OnibusForm

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

def listaviagem(request):
	viagens = Viagem.objects.all()

	ctx = {'viagens': viagens}

	return render(request, 'listaviagem.html', ctx)

##########################################onibus#######################################
def onibus(request):
	dic = {'onibus': []}
	lst = dic['onibus']
	post = lambda x, y: request.POST.get(x,y)

	if request.method == 'POST':
		onibus = {}

		onibus['inputPlaca'] = post('inputPlaca', 'placa não informado')
		onibus['inputCat_veiculo'] = post('inputCat_veiculo', 'categoria não informado')
		onibus['inputLugares'] = post('inputLugares', 'lugar não informado')
		onibus['inputAutonomia'] = post('inputAutonomia', 'autonomia não informado')
		onibus['inputVeic_pronto'] = post('inputVeic_pronto', 'veículo pronto não informado')

		lst.append(onibus)

	




	#Inserir no banco

	form = OnibusForm(request.POST or None)

	if form.is_valid():
		form.save() 
	
	listar_onibus = Onibus.objects.all()
	ctx = {'listar_onibus': listar_onibus}

	return render(request, 'onibus.html', ctx)







##########################################passageiro#######################################
def passageiro(request):
	dic = {'passageiro': []}
	lst = dic['passageiro']
	post = lambda x, y: request.POST.get(x,y)

	if request.method == 'POST':
		passageiro = {}

		passageiro['inputCpf'] = post('inputCpf', 'cpf não informado')
		passageiro['inputNome'] = post('inputNome', 'nome não informado')
		passageiro['inputTelefone'] = post('inputTelefone', 'telefone não informado')
		passageiro['inputEmail'] = post('inputEmail', 'email não informado')
		passageiro['inputPago'] = post('inputPago', 'pagamento não informado')

		lst.append(passageiro)
	return render(request, 'passageiro.html', dic)