from django.contrib import admin
from .models import Cargo, Funcionario, Gênero


# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Gênero)