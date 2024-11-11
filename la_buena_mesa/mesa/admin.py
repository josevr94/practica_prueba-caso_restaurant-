from django.contrib import admin
from .models import Mesa

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de mesas
    list_display = ('n_mesa', 'capacidad', 'ubicacion')
    
    # Campos que se pueden utilizar para buscar
    search_fields = ('n_mesa', 'ubicacion')  # Puedes buscar por número de mesa o ubicación
    
    # Opcionalmente, añade filtros para algunos campos
    list_filter = ('capacidad',)
    
    # Ordenación predeterminada
    ordering = ('n_mesa',)
    
    # Método para mostrar la mesa de forma más legible (opcional)
    def n_mesa(self, obj):
        return f'Mesa {obj.n_mesa}'
    n_mesa.short_description = 'Número de Mesa'
