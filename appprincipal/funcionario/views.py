

# Create your views here.
from appprincipal.funcionario.forms import *
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.db import models, transaction
from appprincipal.funcionario.models import *
from ckeditor.fields import RichTextField
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from appprincipal.funcionario.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required #para Functions Based Views
from django.contrib import messages


from django.urls import reverse_lazy,reverse
#from django.core.urlresovers import reverse_lazy
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views


from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from appprincipal.funcionario.views import *


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = FuncionarioForm(request.POST, instance=request.user.funcionario)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('appprincipal:index')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = FuncionarioForm(instance=request.user.funcionario)
    return render(request, 'funcionario/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


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


class FuncionarioUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "funcionario/atualiza_func.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("appprincipal:index")

class FuncionarioDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "funcionario/exclui_func.html"
    model = Funcionario
    fields = '__all__'

    def get_success_url(self):
        return reverse('appprincipal:index')
    
@login_required
def lista_funcionarios(ListView):
    funcionarios = Funcionario.objects.all()
    
    contexto = {
        'funcionarios': funcionarios
    }

    return render(ListView, "funcionario/funcionarios.html",contexto)

