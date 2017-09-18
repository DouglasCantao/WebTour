from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^painel$', views.paineldecontrole, name='paineldecontrole'),
	url(r'^cadastro$', views.cadastro, name='cadastro'),
]