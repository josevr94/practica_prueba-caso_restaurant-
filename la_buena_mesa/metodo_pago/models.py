from django.db import models

# Create your models here.

class MetododePago(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.tipo
    