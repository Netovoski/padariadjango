from django.contrib import admin

# Register your models here.
from appprincipal.funcionario.models import *

# admin.site.register(TipoProduto)
admin.site.register(TipoCargo)
#admin.site.register(Produto)
admin.site.register(Funcionario)