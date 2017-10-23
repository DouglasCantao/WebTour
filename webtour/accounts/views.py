<<<<<<< HEAD
# coding=utf-8

from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import User
from .forms import UserAdminCreationForm


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')


=======
# coding=utf-8

from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import User
from .forms import UserAdminCreationForm


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')


>>>>>>> 1c6bb3ac3692effaf0ab3562b25a958fcad0a942
register = RegisterView.as_view()