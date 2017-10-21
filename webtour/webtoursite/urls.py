from django.conf.urls import url, include
from . import views


#urlpatterns = [
#	url(r'^$', views.index, name='index'),
#	url(r'^recuperarsenha$', views.recuperarsenha, name='recuperarsenha'),
#	url(r'^painel$', views.paineldecontrole, name='paineldecontrole'),
#	url(r'^cadastro$', views.cadastro, name='cadastro'),
#	url(r'^listaviagem$', views.listaviagem, name='listaviagem'),
#	url(r'^passageiro$', views.passageiro, name='passageiro'),
#	url(r'^contato$', views.contato, name='contato'),
#	url(r'^onibus$', views.onibus, name='onibus'),
#	url(r'^remove_onibus$', views.remove_onibus, name='remove_onibus'),
#	url(r'^remove_passageiro$', views.remove_passageiro, name='remove_passageiro'),
#]


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^entrar$', views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^sair$', views.logout, {'next_page': 'login'}, name='logout'),
	url(r'^painel$', views.paineldecontrole, name='paineldecontrole'),
	#url(r'^cadastro$', views.cadastro, name='cadastro'),
    url(r'^conta/', include('accounts.urls', namespace='accounts')),
	url(r'^listaviagem$', views.listaviagem, name='listaviagem'),
	url(r'^passageiro$', views.passageiro, name='passageiro'),
	url(r'^contato$', views.contato, name='contato'),
	url(r'^onibus$', views.onibus, name='onibus'),
	url(r'^remove_onibus$', views.remove_onibus, name='remove_onibus'),
	url(r'^remove_passageiro$', views.remove_passageiro, name='remove_passageiro'),
]