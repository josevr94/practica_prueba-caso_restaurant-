from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de reservas
    list_display = ('cliente_id', 'mesa_id', 'fecha_reserva', 'estado')
    
    # Campos que se pueden utilizar para buscar
    search_fields = ('cliente_id__nombre', 'mesa_id__n_mesa', 'estado')  # Buscar por nombre del cliente, número de mesa y estado
    
    # Opcionalmente, añade filtros para algunos campos
    list_filter = ('estado', 'fecha_reserva')
    
    # Ordenación predeterminada
    ordering = ('-fecha_reserva',)  # Ordenar por fecha de reserva de más reciente a más antigua
    
    # Mostrar una representación más amigable para el estado (opcional)
    def estado_reserva(self, obj):
        return obj.get_estado_display()
    estado_reserva.short_description = 'Estado de la Reserva'
    
    # Personalización adicional para la fecha (opcional)
    def fecha_reserva_formateada(self, obj):
        return obj.fecha_reserva.strftime('%Y-%m-%d %H:%M')
    fecha_reserva_formateada.short_description = 'Fecha de Reserva'

