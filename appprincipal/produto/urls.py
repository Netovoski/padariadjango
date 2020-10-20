from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path


from appprincipal.produto.views import *

app_name = 'produto'

urlpatterns = [
    
    path('tipoprod/', Cadast_TipoProdCreateView.as_view(), name="tipoprod"),
    path('tipoprod/produto/', Cadast_ProdCreateView.as_view(), name = 'produto'),
    #path('produto/', ListaProdutoListView.as_view(), name = 'lista_produto'),
    path('produto/', views.ProdutoListView, name = "lista_produto"),
    path('produto/<pk>', ProdutoUpdateView.as_view(), name = 'update_prod'),
    path('produto/excluir/<pk>', ProdutoDeleteView.as_view(), name = 'deleta_prod'),
    


]