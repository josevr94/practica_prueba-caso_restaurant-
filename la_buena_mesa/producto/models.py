from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=100,decimal_places=2,default=1)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    