from django.shortcuts import render
# Create your views here.
from appprincipal.vendas.forms import *
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.db import models
from appprincipal.vendas.models import *
from ckeditor.fields import RichTextField
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from appprincipal.vendas.models import *

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required #para Functions Based Views

from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views

from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator


# Create your views here.

class NewVendaCreateView(CreateView):
    template_name = "vendas/nova_venda.html"
    model = Venda
    form_class = RegistrarVendaForm
    success_url = reverse_lazy("appprincipal:venda_produto")
    #@method_decorator(login_required, allowed_users(allowed_roles=['customer']))
    #@method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['admin', 'funcionario','gerente']))
    @method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['funcionario', 'gerente', 'admin']))
    def get (self, request):

        return render(request, self.template_name)


class VendaDeleteView(DeleteView):
    template_name = "vendas/exclui_venda.html"
    model = Produto
    context_object_name =  'produto'
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class VendaCreateView(CreateView):
    template_name = "vendas/venda.html"
    model = Venda_Produto
    context_object_name =  'venda_produtos'
    fields = '__all__'
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get (self, request):

        return render(request, self.template_name)

class VendProdListView(ListView):
    template_name = "vendas/venda_prod.html"
    model = Venda_Produto
    context_object_name = "lista_venda"
    @method_decorator(login_required, allowed_users(allowed_roles=['customer', 'funcionario', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)


class Venda_QuantListView(ListView):
    template_name = "vendas/venda_quant.html"
    model = Venda
    context_object_name = "vendas"
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'customer', 'funcionario', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class ProdutoCreateView(CreateView):
    template_name = "vendas/venda_produto.html"
    model = Venda_Produto
    context_object_name =  'venda_produtos'
    fields = '__all__'
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente', 'funcionario']))
    def get (self, request):

        return render(request, self.template_name)