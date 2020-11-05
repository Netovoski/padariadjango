from django.shortcuts import render
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
from django.db.models import Avg, Sum, Count, F, FloatField
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #para Functions Based Views
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
import ipdb

# Create your views here.

@login_required
def venda_create(request):


    novavenda2 = Venda2(fkfuncionario = request.user)

    #from ipdb import set_trace; set_trace()

    novavenda2.save()


    idvv = novavenda2.id
    #from ipdb import set_trace; set_trace()

    return redirect('vendas:nova_venda', idvenda2 = idvv)


class NovavendaView(CreateView):
    fields = ['fkproduto', 'quantidade', 'precovenda']
    template_name = "vendas/nvenda.html"
    model = Venda_Produto
    
    # def totalunid(self):
		
	# 	return self.quantidade*self.precovenda

    def form_valid(self, form,  **kwargs):

        #from ipdb import set_trace; set_trace()        
        idvendaxxx = self.kwargs['idvenda2']
        vend_prodform = form.save(commit=False)
        vend_prodform.fkvenda_id = idvendaxxx       #passando o id do orçamento 
        self.object = vend_prodform.save() #Salvando e apagando os dados do formulário
        
        return HttpResponseRedirect(self.request.path_info) #retornando para a mesma página
    
    def get_context_data(self, **kwargs):
        ido = self.kwargs['idvenda2']

        produtos = Venda_Produto.objects.filter(fkvenda_id=ido)
        prodcomsoma = produtos.values('quantidade').aggregate(prodcomsoma=Sum("quantidade"))
        valorcomsoma = produtos.values('precovenda').aggregate(valorcomsoma=Sum("precovenda"))
            

        context = super(NovavendaView, self).get_context_data(**kwargs)
        total = Venda_Produto.objects.filter(fkvenda_id=ido).aggregate(total=Sum(F('quantidade')*F('precovenda'),output_field=models.FloatField()))

        context['prods'] = produtos
        context['prodcomsoma'] = prodcomsoma
        context['valorcomsoma'] = valorcomsoma
        context['total'] = total
        
       
        return context


@login_required
def DeletarUnid(request,pk):
    tp = Venda_Produto.objects.get(id=pk)
    venda = tp.fkvenda.id

    tp.delete()
    
    return redirect("vendas:nova_venda", idvenda2=venda)

class VendaDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "vendas/exclui_venda.html"
    model = Venda2
    context_object_name =  'compras'
    
    def get_success_url (self):

        return reverse("vendas:minhasvendas")


@login_required
def CompraListView(request):


    #vendedor = Venda_Produto.objects.get(id=pk)
    #venda = vendedor.fkvenda.id
    compras = Venda2.objects.all()
    venda_produtos = Venda_Produto.objects.all()
    #total = Venda_Produto.objects.all().annotate(total=Sum(F('quantidade')*F('precovenda'),output_field=models.FloatField()))
    #total = Venda_Produto.objects.all().annotate(total=F('quantidade')*F('precovenda'))
    #produtos = Venda_Produto.objects.filter(fkvenda_id=id)
    #prodcomsoma = produtos.values('quantidade').aggregate(prodcomsoma=Sum("quantidade"))
    contexto = {
        'compras': compras,
        #'total' : total,
        #'produto' : produto,
        'venda_produtos' : venda_produtos
    }
    
    return render(request, "vendas/minhas_vendas.html",contexto)

def finalizacompra(request, id):

    try:
        vendedor = Venda_Produto.objects.get(id = vendedor)
        
        venda_produto = Venda_Produto.objects.filter(fkvenda=vendedor).all()
        quantidade_total_produtos = 0
        item = Venda_Produto.objects.all()
    
        args = None
        if compra is None:

            args = {
                'msg': 'Nenhum produto no adcionado',
                'vendedor': vendedor.id
            }
        else:
            args = {
                'item': item,
                'compra': compra,
                'vendedor': vendedor,
                #'valor_total': valor_total_produtos,
                'quantidade_total': quantidade_total_produtos,
        }

    except vendedor.DoesNotExist:
        return reverse("vendas:minhasvendas")
    
    
    return render(request, 'vendas/compras.html', args)
    
