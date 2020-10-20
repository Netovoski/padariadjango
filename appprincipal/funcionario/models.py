from django.db import models


# Create your models here.
class TipoCargo(models.Model):
	nmtipocargo = models.CharField(max_length=50, null=False,blank=False)
	def __str__(self):
		return self.nmtipocargo

class Funcionario(models.Model):

    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField( max_length=255,null=False, blank=False)
    cpf = models.CharField( max_length = 255, null = False, blank= False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    fkcargo =  models.ForeignKey(TipoCargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

