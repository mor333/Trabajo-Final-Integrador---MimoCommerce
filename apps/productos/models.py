from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_vencimiento = models.DateField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre