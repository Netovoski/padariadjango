

# Create your views here.
from appprincipal.funcionario.forms import *
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.db import models
from appprincipal.funcionario.models import *
from ckeditor.fields import RichTextField
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from appprincipal.funcionario.models import *

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required #para Functions Based Views

from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views


from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from appprincipal.funcionario.views import *



class CargoCreateView(CreateView):
    template_name = "funcionario/cadast_cargo.html"
    model = TipoCargo
    form_class = CargoForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['admin']))
    def get (self, request):

        return render(request, self.template_name)

class FuncionarioCreateView(CreateView):
    template_name = "funcionario/cadastrar_func.html"
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['#']))
    def get (self, request):

        return render(request, self.template_name)

#class FuncionarioUpdateView(UpdateView):
  # template_name = "atualiza_func.html"
  #  model = Funcionario
  #  context_object_name = "funcionario"
  #  fields = '__all__'
  #  success_url = reverse_lazy("appprincipal:index")
class FuncionarioUpdateView(UpdateView):
    template_name = "funcionario/atualiza_func.html"
    model = Funcionario
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('index')
    @method_decorator(login_required)
    def get (self, request):

        return render(request, self.template_name)

class ListaFuncionariosListView(ListView):
    template_name = "funcionario/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"
    @method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['__all__']))
    def get (self, request):

        return render(request, self.template_name)
