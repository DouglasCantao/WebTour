from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
	if request.method == 'POST':
		for key, value in request.POST.items():
			print(key, value)

		return render(request, 'paineldecontrole.html')

	return render(request, 'index.html')




def paineldecontrole(request):
	return render(request, 'paineldecontrole.html')
