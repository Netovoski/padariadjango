from django.db import models

# Create your models here.

class TipoProduto(models.Model):
	nmtipoproduto = models.CharField(max_length=50)
	def __str__(self):
		return f'{self.nmtipoproduto}'
	

class Produto(models.Model):
	nmproduto = models.CharField( max_length=50, null=False, blank=False)
	precoprod = models.DecimalField( max_digits=8, decimal_places=2, null=False, blank=False )
    
	fktipoprod = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)


	def __str__(self):
		return f'{self.nmproduto}'
