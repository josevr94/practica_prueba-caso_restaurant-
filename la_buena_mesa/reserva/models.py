from django.db import models
from cliente.models import Cliente
from mesa.models import Mesa
from django.utils import timezone

# Create your models here.
class Reserva(models.Model):
    ESTADO_OPCIONES = [
        ('confirmar','Confirmar'),
        ('cancelar','Cancelar'),
    ]
    cliente_id = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    mesa_id = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(default=timezone.now, help_text='Fecha y hora en la que quieres agendar tu reserva')
    estado = models.CharField(max_length=20,choices=ESTADO_OPCIONES)
    
    def __str__(self):
        return f'Reserva a nombre de: {self.cliente_id.nombre}'
                                            