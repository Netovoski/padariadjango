import datetime
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.db.models import F, Sum
from appprincipal.funcionario.models import *
from appprincipal.produto.models import *
from django.db.models import F, ExpressionWrapper, DecimalField
from django import template
register = template.Library()

# Create your models here.

class Venda2(models.Model):
	fkfuncionario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)

	vdatacriacao = models.DateField(editable=False, null=True)
	vdatamodificacao = models.DateField(editable=False, null=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.vdatacriacao = timezone.now()
		self.vdatamodificacao = timezone.now()
		

		return super(Venda2, self).save(*args, **kwargs)

class Venda_Produto(models.Model):
	fkvenda = models.ForeignKey(Venda2, on_delete=models.CASCADE)
	fkproduto = models.ForeignKey(Produto, on_delete=models.CASCADE)

	quantidade = models.IntegerField(blank=True, null=True) 
	precovenda = models.FloatField(default=1, blank=True, null=True) 

	pdatacriacao = models.DateField(editable=False, null=True)
	pdatamodificacao = models.DateField(editable=False, null=True)
    
	# multtotal = models.FloatField(editable=False)
	#@property
	def total(self):
		
		return self.quantidade * self.precovenda
	
	

	def save(self, *args, **kwargs):
		
		if not self.id:
			self.pdatacriacao = timezone.now()
		self.pdatamodificacao = timezone.now()


		return super(Venda_Produto, self).save(*args, **kwargs)
	


	def save(self, *args, **kwargs):
		
		

		return super(Venda_Produto, self).save(*args, **kwargs)
	# def save(self, *args, **Kwargs)
		
		
	# 	return super(Venda_Produto, self).save(*args, **kwags)


	def __str__(self):
		return str(self.fkproduto)


objects = models.Manager()

# class Venda_Total(models.Model):
# 	multtotal = models.ForeignKey(Venda_Produto, on_delete=models.CASCADE, editable=False)


# 	def save(self, *args, **kwargs):
		
# 		multtotal = self.quantidade * self.precovenda

# 		return super(Venda_Total, self).save(*args, **kwargs)