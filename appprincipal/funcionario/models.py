from django.db import models


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class TipoCargo(models.Model):
	nmtipocargo = models.CharField(max_length=50, null=False,blank=False)
	def __str__(self):
		return self.nmtipocargo

class Funcionario(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField( max_length=255,null=False, blank=False)
    cpf = models.CharField( max_length = 255, null = False, blank= False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=False)
    fkcargo =  models.ForeignKey(TipoCargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

@receiver(post_save, sender=User)
def create_user_func(sender, instance, created, **kwargs):
    if created:
        Funcionario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_func(sender, instance, **kwargs):
    instance.funcionario.save()
