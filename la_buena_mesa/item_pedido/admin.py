from django.contrib import admin
from .models import ItemPedido

# Register your models here.




@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de items de pedido
    list_display = ('pedido_id', 'producto_id', 'cantidad', 'total')
    
    # Campos que se pueden utilizar para buscar
    search_fields = ('pedido_id__id', 'producto_id__nombre')  # suponiendo que "nombre" es un campo en Producto
    
    # Opcionalmente, añade filtros para algunos campos
    list_filter = ('pedido_id', 'producto_id')
    
    # Ordenación predeterminada
    ordering = ('pedido_id',)
    
    # Método personalizado para mostrar el total de cada item (cantidad * precio_unitario)
    def total(self, obj):
        return obj.cantidad * obj.precio_unitario
    total.short_description = 'Total'

