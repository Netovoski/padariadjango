from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class TipoProduto(models.Model):
	nmtipoproduto = models.CharField(max_length=50)
	def __str__(self):
		return f'{self.nmtipoproduto}'
	
class TipoCargo(models.Model):
	nmtipocargo = models.CharField(max_length=50, null=False,blank=False)
	def __str__(self):
		return self.nmtipocargo

class Produto(models.Model):
	nmproduto = models.CharField( max_length=50, null=False, blank=False)
	precoprod = models.DecimalField( max_digits=8, decimal_places=2, null=False, blank=False )
    
	fktipoprod = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.nmproduto}'



class Funcionario(models.Model):

    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField( max_length=255,null=False, blank=False)
    cpf = models.CharField( max_length = 255, null = False, blank= False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    fkcargo =  models.ForeignKey(TipoCargo, on_delete=models.CASCADE)

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