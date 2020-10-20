
# Create your views here.
from appprincipal.produto.forms import *
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.db import models
from appprincipal.produto.models import *
from ckeditor.fields import RichTextField
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from appprincipal.produto.models import *

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required #para Functions Based Views

from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views


from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from appprincipal.produto.views import *



class Cadast_TipoProdCreateView(CreateView):
    template_name = "produto/cadast_prod.html"
    model = TipoProduto
    form_class = RegistrarTipoProdutoForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class Cadast_ProdCreateView(CreateView):
    template_name = "produto/prod_cad.html"
    model = Produto
    form_class = RegistrarProdutoForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class ProdListView(ListView):
    template_name = "produto/vendas.html"
    model = Produto
    context_object_name = "produtos"
    @method_decorator(login_required, allowed_users(allowed_roles=['customer', 'admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)


# class ListaProdutoListView(ListView):
#     template_name = "produto/produtos.html"
#     model = Produto
#     context_object_name = "produtos"
#     @method_decorator(login_required)
#     #@method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
#     def get (self, request):

#         return render(request, self.template_name)
@login_required
def ProdutoListView(ListView):
    produtos = Produto.objects.all()
    
    contexto = {
        'produtos': produtos
    }

    return render(ListView, "produto/produtos.html",contexto)

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "produto/atualiza_prod.html"
    model = Produto
    fields = '__all__'
    context_object_name = "produto"
    success_url = reverse_lazy("appprincipal:index")
    # @method_decorator(login_required)
    # #@method_decorator(allowed_users(allowed_roles=['admin','gerente']))
    # def get (self, request):

    #     return render(request, self.template_name)
    
class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "produto/exclui_prod.html"
    model = Produto
    context_object_name =  'produto'
    #success_url = reverse_lazy("appprincipal:lista_produto")
    #@method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get_success_url (self):

        return reverse("produto:lista_produto")





