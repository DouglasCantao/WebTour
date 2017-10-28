from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^cadastro$', views.cadastro, name='cadastro'),  # TODO
    url(r'^logout$', views.logout, name='logout'),
    url(r'^painel$', views.paineldecontrole, name='paineldecontrole'),
    #url(r'^conta/', include('accounts.urls', namespace='accounts')),
    url(r'^listaviagem$', views.listaviagem, name='listaviagem'),
    url(r'^passageiro$', views.passageiro, name='passageiro'),
    url(r'^contato$', views.contato, name='contato'),
    url(r'^onibus$', views.onibus, name='onibus'),
    url(r'^remove_onibus$', views.remove_onibus, name='remove_onibus'),
    url(r'^remove_passageiro$', views.remove_passageiro, name='remove_passageiro'),
    url(r'^cadastrarviagem$', views.cadastrarViagem, name='cadastrarviagem'),
]
