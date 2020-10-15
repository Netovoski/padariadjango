from appprincipal.vendas.models import *
from appprincipal.vendas.views import *
from django import forms
from django.forms import ModelForm

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistrarVendaForm(forms.ModelForm):
    
    class Meta:
        model = Venda

        fields = [
            'vendedor',
            
            
        ]

class VendaForm(forms.ModelForm):
    class meta:
        model = Venda
        

        fields = [
            '__all__'
        ]

class Venda_ProdutoForm(forms.ModelForm):
    class meta:
        model = Venda_Produto

        fields = [
            '__all__'
        ]
