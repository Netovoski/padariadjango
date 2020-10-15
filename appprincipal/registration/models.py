from django.db import models

from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from appprincipal.funcionario.models import *
from appprincipal.produto.models import *
from appprincipal.funcionario.models import *


class Cliente(models.Model):
	user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
	nome = models.CharField(max_length=200, null=True)
	tel = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	data_criada = models.DateTimeField(auto_now_add= True, null=True)
		
	def __str__(self):
		return self.nome

