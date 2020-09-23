from projpad.models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CargoForm(forms.ModelForm):

    class Meta:
        model = TipoCargo

        fields = [
            'nmtipocargo',
        ]

class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario

        fields = [
            'fkcargo',
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao',
        ]


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

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']