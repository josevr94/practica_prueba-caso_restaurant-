from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField( max_length=15, unique=True)
    email = models.EmailField( unique=True, blank=True,null=True  )
    direccion = models.TextField(max_length=250, blank=True,null=True)
    
    def __str__(self):
        return self.nombre
    