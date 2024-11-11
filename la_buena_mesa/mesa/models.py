from django.db import models

# Create your models here.
class Mesa(models.Model):
    n_mesa = models.PositiveIntegerField(default=1)
    capacidad = models.PositiveIntegerField(default=1)
    ubicacion = models.TextField()
    
    def __str__(self):
        return str(self.n_mesa)
    
    
    
    