from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de productos
    list_display = ('nombre', 'precio_unitario','descripcion')
    
    # Campos que se pueden utilizar para buscar
    search_fields = ('nombre', 'descripcion')
    
    # Opcionalmente, añade filtros para algunos campos (si es relevante en tu modelo)
    # list_filter = ('campo',)
    
    # Ordenación predeterminada
    ordering = ('nombre',)