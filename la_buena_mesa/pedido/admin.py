from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de pedidos
    list_display = ('reserva_id', 'cliente_id', 'total', 'fecha_pedido', 'estado')
    
    # Campos que se pueden utilizar para buscar
    search_fields = ('reserva_id__id', 'cliente_id__nombre', 'estado')  # Suponiendo que "nombre" es un campo en Cliente
    
    # Opcionalmente, añade filtros para algunos campos
    list_filter = ('estado', 'fecha_pedido')
    
    # Ordenación predeterminada
    ordering = ('-fecha_pedido',)  # Ordenar de más reciente a más antiguo
    
    # Mostrar una representación más amigable para el estado (opcional)
    def estado_pedido(self, obj):
        return obj.get_estado_display()
    estado_pedido.short_description = 'Estado del Pedido'

    # Personalizar la representación en el admin de la fecha
    def fecha_pedido_formateada(self, obj):
        return obj.fecha_pedido.strftime('%Y-%m-%d %H:%M')
    fecha_pedido_formateada.short_description = 'Fecha del Pedido'
