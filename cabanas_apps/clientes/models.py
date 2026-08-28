"""
Modelos de la aplicación Clientes.
"""

from django.db import models
from django.core.validators import RegexValidator


class Cliente(models.Model):
    """Modelo que representa un cliente del sistema."""

    id = models.AutoField(primary_key=True)
    dni = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(r'^\d{1,20}$', 'El DNI debe contener solo números (máx. 20).')],
        verbose_name="DNI"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    direccion = models.CharField(max_length=200, blank=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["apellido", "nombre"]

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"

    def nombre_completo(self) -> str:
        """Devuelve el nombre completo del cliente."""
        return f"{self.nombre} {self.apellido}"

    def actualizar(self, **datos):
        """Actualiza la instancia actual con los datos proporcionados."""
        for campo, valor in datos.items():
            setattr(self, campo, valor)
        self.save(update_fields=list(datos.keys()) if datos else None)
        return self

    def eliminar(self):
        """Elimina la instancia actual."""
        return self.delete()
