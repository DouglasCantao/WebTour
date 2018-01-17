#-*- coding: UTF-8 -*-

# Python
from decimal import Decimal

# Django.
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.forms import modelformset_factory

# Webtoursite
from webtoursite.models import Viagem, Onibus, Passageiro, Motorista

## Decorators
def acesso_autenticado(func):
    def func_wrapper(request):
        if request.user.is_authenticated:
            return func(request)

        return redirect('login')

    return func_wrapper

def login(request):
    if request.POST:
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']

        usuario = authenticate(request, username=nome_usuario, password=senha)

        if usuario is not None:
            django_login(request, usuario)
            # Redirect to a success page.
            return redirect('paineldecontrole')

        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    django_logout(request)

    return redirect('login')

def cadastro(request):
    if request.method == 'POST':
        # Validar os campos enviados.
        for key, value in request.POST.items():
            print(key, value)

        # Caso valide, criar e salvar um usuário no banco de dados e
        # redirecionar para a tela de painel de controle (fazer o login do
        # Django).
        lst = User.objects.filter(username=request.POST['usuario'])
        lst_email = User.objects.filter(email=request.POST['email'])
        usr = User()

        # Se o username já estiver sendo utilizado.
        # TODO: Tratar erro na tela (tem que enviar a informação e exibir)
        if(lst.count() > 0):
          ctx ={"erro_user": 'Nome de usuário indisponível', "erro_email": 'E-mail já está cadastrado.'}
        elif(lst_email.count() > 0):
          ctx ={"erro_email": 'E-mail já está cadastrado.'}
          return render(request, 'cadastro.html', ctx)
        # Salva o usuário no banco.
        usr.username = request.POST['usuario']
        usr.first_name = request.POST['nome']
        usr.last_name = request.POST['sobrenome']
        usr.email = request.POST['email']
        usr.set_password(request.POST['senha'])
        usr.save()

        django_login(request, usr)

        return redirect('paineldecontrole')

    return render(request, 'cadastro.html')


@acesso_autenticado
def paineldecontrole(request):
    return render(request, 'paineldecontrole.html')



def profile(request):
  return render(request, 'profile.html')
























def contato(request):
         return render(request, 'contato.html')


@acesso_autenticado
def listaviagem(request):

  viagens = Viagem.objects.filter(dono_id=request.user.id)
  ctx = {'viagens': viagens}

  return render(request, 'listaviagem.html', ctx)

@acesso_autenticado
def onibus(request):
    dic = {'onibus': Onibus(), 'lista_onibus':[], 'errors': {}}

    # Recupera lista de ônibus cadastrados do banco de dados.
    dic['lista_onibus'] = Onibus.objects.filter(dono_id=request.user.id)

    if request.method == 'POST':
        post = lambda x, y: request.POST.get(x,y)

        # Inserindo os valores do formulário no objeto ônibus.
        dic['onibus'].placa = post('inputPlaca', '')
        dic['onibus'].categoria = post('inputCat_veiculo', 'Ônibus')
        dic['onibus'].qtde_lugares = int(post('inputLugares', 0))
        dic['onibus'].autonomia = Decimal(post('inputAutonomia', '0.00'))
        dic['onibus'].veic_pronto = post('inputVeic_pronto', 'True')
        dic['onibus'].dono_id = request.user.id

        # Validação dos campos.
        if not dic['onibus'].placa:
            dic['errors']['inputPlaca'] = "Favor informar a placa."

        if not dic['onibus'].qtde_lugares:
            dic['errors']['inputLugares'] = "Favor informar a quantidade de assentos."

        elif dic['onibus'].categoria == 'Ônibus' and not (0 < dic['onibus'].qtde_lugares <= 47):
            dic['errors']['inputLugares'] = "Somente ônibus com até 47 lugares."

        elif dic['onibus'].categoria == 'Microônibus' and not (0 < dic['onibus'].qtde_lugares <= 20):
            dic['errors']['inputLugares'] = "Somente microônibus com até 20 lugares."

        elif dic['onibus'].categoria == 'Van' and not (0 < dic['onibus'].qtde_lugares <= 16):
            dic['errors']['inputLugares'] = "Somente van com até 16 lugares."

        if dic['onibus'].autonomia > Decimal('25.00') or dic['onibus'].autonomia < Decimal('0.00'):
            dic['errors']['inputAutonomia'] = 'A autonomia deve ser um valor entre 0 e 25.00'

        if dic['errors']:
            dic['onibus'].autonomia = post('inputAutonomia', '0.00')

        # Se os campos tiverem sido validados, salvar no banco e limpar o formulário.
        if not dic['errors']:
            dic['onibus'].save()
            dic['onibus'] = Onibus()

    return render(request,'onibus.html', dic)

# Remover dados do banco
def remove_onibus(request):
         if 'id_onibus' in request.POST:
                  obj = Onibus.objects.get(pk=int(request.POST['id_onibus']))
                  obj.delete()

                  return HttpResponse('Removido com sucesso.')






###########################################passageiro#######################################
@acesso_autenticado
def passageiro(request):
         dic = {'passageiro': Passageiro(), 'lista_passageiro':[]}
         dic['lista_passageiro'] = Passageiro.objects.filter(dono_id=request.user.id)



         if request.method == 'POST':
                  post = lambda x, y: request.POST.get(x,y)

                  dic['passageiro'].cpf = post('inputCpf', '99665544331')
                  dic['passageiro'].nome = post('inputNome', 'Sebastiana')
                  dic['passageiro'].telefone = post('inputTelefone', '31988457474')
                  dic['passageiro'].email = post('inputEmail', 'pedro@viagens.com.br')
                  dic['passageiro'].dono_id = request.user.id

                  dic['passageiro'].save()
                  dic['passageiro'] = Passageiro()

         return render(request, 'passageiro.html', dic)

#remove passageiro do banco
def remove_passageiro(request):
         if 'id_passageiro' in request.POST:
                  obj = Passageiro.objects.get(pk=int(request.POST['id_passageiro']))
                  obj.delete()

         return HttpResponse('Removido com sucesso.')


##############################recuperar senha##########################################
def recuperarsenha(request):
    return render(request, 'recuperarsenha.html')


##################### Contato #############################
def contato(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contato.html', context)

####################################################cadastro viagem

@acesso_autenticado
def cadastrarViagem(request):
  #Passando apenas os ônibus referente ao usuário logado para a modal
  onibus = Onibus.objects.filter(dono_id=request.user.id)
  


  #Exibir viagem cadastradas
  dic = {'viagem': Viagem(), 'lista_viagem':[]}

  dic['lista_viagem'] = Viagem.objects.filter(dono_id=request.user.id)


  ctx = {'onibus': onibus, 'lista_viagem_banco': dic['lista_viagem']}


  if request.method == 'POST':
    post = lambda x, y: request.POST.get(x,y)

    dic['viagem'].nome_empresa = post('inputPlaca', '')
    dic['viagem'].origem = post('inputOrigem', '')
    dic['viagem'].destino = post('inputDestino', '')
    dic['viagem'].data_saida = post('inputDataSaida', '')
    dic['viagem'].hora_saida = post('inputHoraSaida', '')
    dic['viagem'].hora_chegada = post('inputHoraChegada', '')
    dic['viagem'].dono_id = request.user.id
    
    dic['viagem'].save()
    dic['viagem'] = Viagem()


  return render(request, 'cadastrar-viagem.html', ctx)

@acesso_autenticado
def motorista(request):
    dic = {'motorista': Motorista(), 'lista_motorista':[]}

    dic['lista_motorista'] = Motorista.objects.filter(dono_id=request.user.id)

    if request.method == 'POST':
        post = lambda x, y: request.POST.get(x,y)

        dic['motorista'].cnh = post('inputCnh', '')
        dic['motorista'].nome = post('inputNome', '')
        dic['motorista'].telefone = post('inputTelefone', '')
        dic['motorista'].email = post('inputEmail', '')
        dic['motorista'].dono_id = request.user.id

        dic['motorista'].save()
        dic['motorista'] = Motorista()
    return render(request, 'motorista.html', dic)

def remove_motorista(request):
    if 'id_motorista' in request.POST:
        obj = Motorista.objects.get(pk=int(request.POST['id_motorista']))
        obj.delete()

    return HttpResponse('Removido com sucesso.')



#remove viagem do banco
def remove_viagem(request):
         if 'id_viagem' in request.POST:
                  obj = Viagem.objects.get(pk=int(request.POST['id_viagem']))
                  obj.delete()

         return HttpResponse('Removido com sucesso.')

def futuro(request):
  return render(request, 'futuro.html')