from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo', 'cpf', 'data_nascimento')
    list_filter = ('tipo',)
    search_fields = ('username', 'email', 'cpf')
