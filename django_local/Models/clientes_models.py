"""
cliente_models.py
Modelos para la gestión de clientes en el sistema de Cabanas.
Incluye definiciones de Cliente y posibles extensiones.
Cumple con estándares Pylint y buenas prácticas de Django.
"""

from django.db import models


class Cliente(models.Model):
    """
    Representa un cliente que interactúa con el sistema.
    """
    nombre = models.CharField(
        max_length=100,
        help_text="Nombre completo del cliente."
    )
    apellido = models.CharField(
        max_length=100,
        help_text="Apellido del cliente."
    )
    dni = models.CharField(
        max_length=20,
        unique=True,
        help_text="Documento nacional de identidad o equivalente."
    )
    email = models.EmailField(
        unique=True,
        help_text="Correo electrónico del cliente."
    )
    telefono = models.CharField(
        max_length=20,
        blank=True,
        help_text="Número de teléfono de contacto."
    )
    direccion = models.TextField(
        blank=True,
        help_text="Dirección física del cliente."
    )
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha en la que el cliente fue registrado en el sistema."
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"