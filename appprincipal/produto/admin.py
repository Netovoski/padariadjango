from django.contrib import admin

# Register your models here.
from appprincipal.produto.models import *

admin.site.register(TipoProduto)

admin.site.register(Produto)
