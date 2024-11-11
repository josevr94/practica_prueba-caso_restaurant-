from django.contrib import admin
from .models import MetododePago

@admin.register(MetododePago)
class MetododePagoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de métodos de pago
    list_display = ('tipo', 'descripcion')
    
    # Campos que se pueden utilizar para buscar
    search_fields = ('tipo', 'descripcion')
    
    # Opcionalmente, añade filtros para algunos campos
    list_filter = ('tipo',)
    
    # Ordenación predeterminada
    ordering = ('tipo',)
    
    # Mostrar el nombre del tipo de pago en el listado (opcional)
    def tipo_pago(self, obj):
        return obj.tipo
    tipo_pago.short_description = 'Tipo de Pago'
