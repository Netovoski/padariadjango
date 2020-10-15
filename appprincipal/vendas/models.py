from django.db import models
from appprincipal.funcionario.models import *
from appprincipal.produto.models import *
import datetime
# Create your models here.
class Venda(models.Model):

	vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    
	def __str__(self):
		return  'Venda '+ str(self.id) +' vendedor '+ str(self.vendedor)

class Venda_Produto(models.Model):
    fkvenda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    fkproduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField(blank=True, null=True) 
    data = models.DateField(default=datetime.date.today())

    def __str__(self):
        return str(self.fkvenda) +' prod. '+ str(self.fkproduto)


objects = models.Manager()