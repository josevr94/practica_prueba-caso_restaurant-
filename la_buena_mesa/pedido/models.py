from django.db import models
from reserva.models import Reserva
from cliente.models import Cliente
from django.utils import timezone
from metodo_pago.models import MetododePago

# Create your models here.
class Pedido( models.Model):
    ESTADO_OPCIONES = [
        ('En preparacion','En preparacion'),
        ('Enviado','Enviado'),
        ('Confirmado','confirmado')
    ]
    reserva_id =  models.OneToOneField(Reserva,on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetododePago,on_delete=models.CASCADE,default='')
    total = models.PositiveIntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20,choices=ESTADO_OPCIONES)
    
    

    