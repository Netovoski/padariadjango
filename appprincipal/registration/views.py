from django.shortcuts import render
from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse
from appprincipal.registration.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views
from django.contrib.auth.forms import UserCreationForm #formulario Users
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator

from appprincipal.registration.forms import *
from django.views.generic.edit import UpdateView 
from django.contrib import messages
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
import json
import datetime

from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse

from appprincipal.registration.models import *

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, "Cadastro realizado com sucesso!"+ username)

			return redirect('registration:login')
			

	context = {'form':form}
	return render(request, 'registration/registrar.html', context)


@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect("appprincipal:index")
		else:
			messages.info(request, "Usuario ou senha incorreta")

	context = {}
	return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect("registration:login")

