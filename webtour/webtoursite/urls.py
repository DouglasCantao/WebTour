from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^entrar$', views.entrar, name='entrar'),
	url(r'^painel$', views.paineldecontrole, name='paineldecontrole'),
	url(r'^cadastro$', views.cadastro, name='cadastro'),
	url(r'^onibus$', views.onibus, name='onibus'),
	url(r'^passageiro$', views.passageiro, name='passageiro'),
	url(r'^contato$', views.contato, name='contato'),
]