from django.db import models

class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    precio_por_cabana = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
