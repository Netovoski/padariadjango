from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path


from appprincipal.vendas.views import *

app_name = 'vendas'

urlpatterns = [

    path('minhasvendas/', VendProdListView.as_view(), name="lista"),
    path('quantidade/', Venda_QuantListView.as_view(), name="venda_quant"),
    path('novavenda/', NewVendaCreateView.as_view(), name ="nova_venda"),
    path('novavenda/<pk>', VendaCreateView.as_view(), name ="cria_venda"),
    path('minhasvendas/excluir/<pk>', VendaDeleteView.as_view(), name = 'deleta_venda'),
    path('listavenda/', VendProdListView.as_view(), name="lista_venda"),
    path('produtovenda/', ProdutoCreateView.as_view(), name = 'venda_produto'),
]