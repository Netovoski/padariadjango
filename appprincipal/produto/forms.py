from appprincipal.produto.models import *
from appprincipal.produto.views import *
from django import forms
from django.forms import ModelForm

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrarTipoProdutoForm(forms.ModelForm):
    
    class Meta:
        model = TipoProduto

        fields = [
            'nmtipoproduto',
        ]

class RegistrarProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto

        fields = [
            'nmproduto',
            'precoprod',
            'fktipoprod',
        ]
