#from core.views import LocaisList, IndexTemplateView, LocalDetailView, RegCreateView, Pt1CreateView
from . import views
from appprincipal.views import IndexTemplateView,  AboutView, TermoView, PolView, ContView,  NewVendaCreateView, ProdListView, RegistrarTipoProdutoForm, Cadast_TipoProdCreateView
from django.urls import path
from appprincipal.views import *

app_name = 'appprincipal'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name = 'index'),
    path('about/', AboutView.as_view(), name = "about"),
    path('minhasvendas/', VendProdListView.as_view(), name="lista"),
    path('quantidade/', Venda_QuantListView.as_view(), name="venda_quant"),
    path('cargo/funcionario', FuncionarioCreateView.as_view(), name="func_cad"),
    path('cargo/', CargoCreateView.as_view(), name="cargo"),
    path('novavenda/', NewVendaCreateView.as_view(), name ="nova_venda"),
    path('novavenda/<pk>', VendaCreateView.as_view(), name ="cria_venda"),
    path('termo_cond/', TermoView.as_view(), name="termo_cond"),
    path('pol/', PolView.as_view(), name="pol"),
    path('cont/', ContView.as_view(), name="cont"),
    path('minhasvendas/excluir/<pk>', VendaDeleteView.as_view(), name = 'deleta_venda'),
    path('tipoprod/', Cadast_TipoProdCreateView.as_view(), name="tipoprod"),
    path('tipoprod/produto/', Cadast_ProdCreateView.as_view(), name = 'produto'),
    path('produto/', ListaProdutoListView.as_view(), name = 'lista_produto'),
    path('produto/<pk>', ProdutoUpdateView.as_view(), name = 'update_prod'),
    path('produto/excluir/<pk>', ProdutoDeleteView.as_view(), name = 'deleta_prod'),
    path('listavenda/', VendProdListView.as_view(), name="lista_venda"),
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="update_func"),
    path('funcionario/', ListaFuncionariosListView.as_view(), name="lista_funcionarios"),
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name = 'deleta_funcionario'),
    path('produtovenda/', ProdutoCreateView.as_view(), name = 'venda_produto'),
    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    

]