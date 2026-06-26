from django.db import models

# Ejemplo de modelo inicial
class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre
