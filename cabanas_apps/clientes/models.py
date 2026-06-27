""" archivo de modelos para la app de clientes """
from django.db import models
from django.core.validators import RegexValidator

class Cliente(models.Model):
    """ Modelo que representa un cliente """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    dni = models.CharField(
        max_length=20,
        unique=True,          # obligatorio y único, pero no clave primaria
        validators=[RegexValidator(r'^\d{1,20}$', 'El DNI debe contener solo números (máx. 20).')]
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"
