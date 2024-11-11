from django.db import models
from pedido.models import Pedido
from producto.models import Producto

# Create your models here.
class ItemPedido(models.Model):
    pedido_id = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    # precio_unitario = models.DecimalField(max_digits=100,decimal_places=2)