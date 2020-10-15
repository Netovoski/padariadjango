
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path


from appprincipal.funcionario.views import *

app_name = 'funcionario'

urlpatterns = [
    
    path('cargo/funcionario', FuncionarioCreateView.as_view(), name="func_cad"),
    path('cargo/', CargoCreateView.as_view(), name="cargo"),
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="update_func"),
    path('funcionario/', ListaFuncionariosListView.as_view(), name="lista_funcionarios"),

]