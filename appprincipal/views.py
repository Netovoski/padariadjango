from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse
from projpad.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views
from django.contrib.auth.forms import UserCreationForm #formulario Users
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator

from appprincipal import views
from appprincipal.forms import *
from django.views.generic.edit import UpdateView 
from django.contrib import messages
from appprincipal.decorators import unauthenticated_user, allowed_users, admin_only
import json
import datetime


# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "index.html"
    @method_decorator(login_required, allowed_users(allowed_roles=['customer']))
    def get (self, request):
        return render(request, self.template_name)

class ProdListView(ListView):
    template_name = "vendas.html"
    model = Produto
    context_object_name = "produtos"
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class AboutView(View):
    template = "about.html"
    @method_decorator(login_required, admin_only)
    def get (self, request):

        return render(request, self.template)


class Cadast_TipoProdCreateView(CreateView):
    template_name = "cadast_prod.html"
    model = TipoProduto
    form_class = RegistrarTipoProdutoForm
    success_url = reverse_lazy("appprincipal:produto")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class Cadast_ProdCreateView(CreateView):
    template_name = "prod_cad.html"
    model = Produto
    form_class = RegistrarProdutoForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class ProdListView(ListView):
    template_name = "vendas.html"
    model = Produto
    context_object_name = "produtos"
    @method_decorator(login_required, allowed_users(allowed_roles=['customer', 'admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class CargoCreateView(CreateView):
    template_name = "cadast_cargo.html"
    model = TipoCargo
    form_class = CargoForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get (self, request):

        return render(request, self.template_name)

class FuncionarioCreateView(CreateView):
    template_name = "cadastrar_func.html"
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get (self, request):

        return render(request, self.template_name)

class NewVendaCreateView(CreateView):
    template_name = "nova_venda.html"
    model = Venda
    form_class = RegistrarVendaForm
    success_url = reverse_lazy("appprincipal:venda_produto")
    #@method_decorator(login_required, allowed_users(allowed_roles=['customer']))
    #@method_decorator(login_required)
    #@method_decorator(allowed_users(allowed_roles=['admin', 'funcionario','gerente']))
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['funcionario', 'gerente', 'admin']))
    def get (self, request):

        return render(request, self.template_name)

class TermoView(View):
    template = "termo.html"
    def get (self, request):

        return render(request, self.template)

class PolView(View):
    template = "pol.html"
    def get (self, request):

        return render(request, self.template)

class ContView(View):
    template = "cont.html"
    def get (self, request):

        return render(request, self.template)

class VendaDeleteView(DeleteView):
    template_name = "exclui_venda.html"
    model = Produto
    context_object_name =  'produto'
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class VendaCreateView(CreateView):
    template_name = "venda.html"
    model = Venda_Produto
    context_object_name =  'venda_produtos'
    fields = '__all__'
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get (self, request):

        return render(request, self.template_name)

class VendProdListView(ListView):
    template_name = "venda_prod.html"
    model = Venda_Produto
    context_object_name = "lista_venda"
    @method_decorator(login_required, allowed_users(allowed_roles=['customer', 'funcionario', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)
#class FuncionarioUpdateView(UpdateView):
  # template_name = "atualiza_func.html"
  #  model = Funcionario
  #  context_object_name = "funcionario"
  #  fields = '__all__'
  #  success_url = reverse_lazy("appprincipal:index")
class FuncionarioUpdateView(UpdateView):
    template_name = "atualiza_func.html"
    model = Funcionario
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('index')
    @method_decorator(login_required)
    def get (self, request):

        return render(request, self.template_name)

class ListaFuncionariosListView(ListView):
    template_name = "funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin']))
    def get (self, request):

        return render(request, self.template_name)


class ListaProdutoListView(ListView):
    template_name = "produtos.html"
    model = Produto
    context_object_name = "produtos"
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class ProdutoUpdateView(UpdateView):
    template_name = "atualiza_prod.html"
    model = Produto
    context_object_name = "produto"
    fields = '__all__'
    success_url = reverse_lazy("appprincipal:lista_produto")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin','gerente']))
    def get (self, request):

        return render(request, self.template_name)

class ProdutoDeleteView(DeleteView):
    template_name = "exclui_prod.html"
    model = Produto
    context_object_name =  'produto'
    success_url = reverse_lazy("appprincipal:lista_produto")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class Venda_QuantListView(ListView):
    template_name = "venda_quant.html"
    model = Venda
    context_object_name = "vendas"
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'customer', 'funcionario', 'gerente']))
    def get (self, request):

        return render(request, self.template_name)

class ProdutoCreateView(CreateView):
    template_name = "venda_produto.html"
    model = Venda_Produto
    context_object_name =  'venda_produtos'
    fields = '__all__'
    success_url = reverse_lazy("appprincipal:index")
    @method_decorator(login_required)
    @method_decorator(allowed_users(allowed_roles=['admin', 'gerente', 'funcionario']))
    def get (self, request):

        return render(request, self.template_name)

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

			return redirect('appprincipal:login')
		

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
    return redirect("appprincipal:login")


