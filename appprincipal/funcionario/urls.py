from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path


from appprincipal.funcionario.views import *

app_name = 'funcionario'

urlpatterns = [
    

    path('cargo/profile', views.update_profile, name='upprofile'),
    path('cargo/funcionario', FuncionarioCreateView.as_view(), name="func_cad"),
    path('cargo/', CargoCreateView.as_view(), name="cargo"),
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="update_func"),
    path('funcionario/', views.lista_funcionarios, name = "lista_funcionarios"),
    path('funcionario/delete/<pk>', FuncionarioDeleteView.as_view(), name="delete_funcionario"),
]