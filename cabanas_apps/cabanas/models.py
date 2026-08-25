""" models"""
from django.db import models

class Cabana(models.Model):  
    """ class cabana"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        """ class meta"""
        verbose_name = "Cabana"
        verbose_name_plural = "Cabanas"

    def __str__(self):
        return str(self.nombre)


# Compatibilidad con código antiguo que espera un modelo llamado 'Cabanas'
# Definir un proxy que reutilice la misma tabla para evitar crear nuevas migraciones.
class Cabanas(Cabana):
    class Meta:
        proxy = True
        verbose_name = "Cabanas"
        verbose_name_plural = "Cabanas"
