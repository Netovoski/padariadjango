from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path
from . import views

from appprincipal.vendas.views import *

app_name = 'vendas'

urlpatterns = [
	path('addvenda/', views.venda_create, name='add_venda'),

    path('novavenda/<int:idvenda2>', NovavendaView.as_view(), name ="nova_venda"),
    path('novavenda/excluir/<pk>',views.DeletarUnid, name='deletarunid'),
    path('minhasvendas/', CompraListView.as_view(), name='minhasvendas'),
    path('minhasvendas/excluir/<pk>', VendaDeleteView.as_view(), name='deletarvenda'),
    #path('compras/<pk>', views.finalizaCompra, name = 'compra_produtos'),
    path('compras/', FinalizaCompraListView.as_view(), name = 'compra_produtos'),

  
]

