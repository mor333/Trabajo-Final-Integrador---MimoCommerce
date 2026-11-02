from django.conf import settings
from django.db import models

# Create your models here.
class Turno(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    nombre_cliente = models.CharField(max_length=150, blank=True, default='')
    servicio = models.ForeignKey('servicios.Servicio', on_delete=models.PROTECT)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=10)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return self.servicio.nombre + ' - ' + str(self.fecha) + ' ' + str(self.hora)