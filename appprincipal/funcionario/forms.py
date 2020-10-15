from appprincipal.funcionario.models import *
from appprincipal.funcionario.views import *
from django import forms
from django.forms import ModelForm


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