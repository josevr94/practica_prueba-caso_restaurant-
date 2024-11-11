from django.contrib import admin
from .models import Cliente
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de clientes
    list_display = ('nombre', 'telefono', 'email', 'direccion')
    
    # Campos que se pueden utilizar para buscar
    search_fields = ('nombre', 'telefono', 'email')
    
    # Opcionalmente, añade filtros para algunos campos
    list_filter = ('direccion',)
    
    # Ordenación predeterminada
    ordering = ('nombre',)