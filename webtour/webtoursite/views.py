from decimal import Decimal

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory

from webtoursite.models import Viagem, Onibus, Passageiro


###############
from django.contrib.auth.forms import UserCreationForm

from webtoursite.models import Viagem, Onibus
from webtoursite.forms import OnibusForm
import functools
import warnings

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.utils.deprecation import (
    RemovedInDjango20Warning,
)
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.six.moves.urllib.parse import urlparse, urlunparse
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import ContactForm



def index(request):
	return render(request, 'index.html')

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
	dic = {'onibus': Onibus(), 'lista_onibus':[], 'errors': {}}

	# Recupera lista de ônibus cadastrados do banco de dados.
	dic['lista_onibus'] = Onibus.objects.all()

	
	if request.method == 'POST':
		post = lambda x, y: request.POST.get(x,y)

		# Inserindo os valores do formulário no objeto ônibus.
		dic['onibus'].placa = post('inputPlaca', '')
		dic['onibus'].categoria = post('inputCat_veiculo', 'Ônibus')
		dic['onibus'].qtde_lugares = int(post('inputLugares', 0))
		dic['onibus'].autonomia = Decimal(post('inputAutonomia', '0.00'))
		dic['onibus'].veic_pronto = post('inputVeic_pronto', 'True')

		# Validação dos campos.
		if not dic['onibus'].placa:
			dic['errors']['inputPlaca'] = "Favor informar a placa."

			if not dic['onibus'].qtde_lugares:
				dic['errors']['inputLugares'] = "Favor informar a quantidade de assentos."

			else:
				if dic['onibus'].categoria == 'Ônibus' and not (0 < dic['onibus'].qtde_lugares <= 47):
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
			#dic['lista_onibus'].append(dic['onibus'])
			dic['onibus'] = Onibus()

			return render(request,'onibus.html', dic)

# Remover dados do banco
def remove_onibus(request):
	if 'id_onibus' in request.POST:
		obj = Onibus.objects.get(pk=int(request.POST['id_onibus']))
		obj.delete()

		return HttpResponse('Removido com sucesso.')






###########################################passageiro#######################################
def passageiro(request):
	dic = {'passageiro': Passageiro(), 'lista_passageiro':[]}

	dic['lista_passageiro'] = Passageiro.objects.all()



	if request.method == 'POST':
		post = lambda x, y: request.POST.get(x,y)

		dic['passageiro'].cpf = post('inputCpf', '99665544331')
		dic['passageiro'].nome = post('inputNome', 'Sebastiana')
		dic['passageiro'].telefone = post('inputTelefone', '31988457474')
		dic['passageiro'].email = post('inputEmail', 'pedro@viagens.com.br')

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
<<<<<<< HEAD
	def recuperarsenha(request):
=======
def recuperarsenha(request):
>>>>>>> 1c6bb3ac3692effaf0ab3562b25a958fcad0a942
		return render(request, 'recuperarsenha.html')


	####################################################login e logout####################


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


def logout(request, next_page=None,
           template_name='registration/logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)

    if next_page is not None:
        next_page = resolve_url(next_page)

    if (redirect_field_name in request.POST or
            redirect_field_name in request.GET):
        next_page = request.POST.get(redirect_field_name,
                                     request.GET.get(redirect_field_name))
        # Security check -- don't allow redirection to a different host.
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path

    if next_page:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page)

    current_site = get_current_site(request)
    context = {
        'site': current_site,
        'site_name': current_site.name,
        'title': _('Logged out')
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)

#################### Cadastro ####################
User = get_user_model()

#class RegisterView(CreateView):
	
	#form_class = UserCreationForm
	#template_name = 'cadastro.html'
	#model = User
	#success_url = reverse_lazy('login')

#cadastro = RegisterView.as_view()

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

####################################################

