"""
cabanas_models.py
Modelos principales para la gestión de cabañas en el sistema.
Incluye definiciones de Cabaña, Cliente y Reserva.
Cumple con estándares Pylint y buenas prácticas de Django.
"""

from django.db import models


class Cabana(models.Model):
    """
    Representa una cabaña disponible en el complejo.
    """
    nombre = models.CharField(
        max_length=100,
        unique=True,
        help_text="Nombre identificador de la cabaña."
    )
    capacidad = models.PositiveIntegerField(
        help_text="Número máximo de huéspedes que admite la cabaña."
    )
    descripcion = models.TextField(
        blank=True,
        help_text="Descripción breve de la cabaña."
    )
    precio_noche = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Precio por noche en moneda local."
    )
    disponible = models.BooleanField(
        default=True,
        help_text="Indica si la cabaña está disponible para reservas."
    )

    class Meta:
        verbose_name = "Cabaña"
        verbose_name_plural = "Cabañas"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} (Capacidad: {self.capacidad})"


class Cliente(models.Model):
    """
    Representa un cliente que realiza reservas.
    """
    nombre = models.CharField(max_length=100, help_text="Nombre completo del cliente.")
    email = models.EmailField(unique=True, help_text="Correo electrónico del cliente.")
    telefono = models.CharField(max_length=20, blank=True, help_text="Teléfono de contacto.")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    """
    Representa una reserva realizada por un cliente en una cabaña.
    """
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="reservas",
        help_text="Cliente que realiza la reserva."
    )
    cabana = models.ForeignKey(
        Cabana,
        on_delete=models.CASCADE,
        related_name="reservas",
        help_text="Cabaña reservada."
    )
    fecha_inicio = models.DateField(help_text="Fecha de inicio de la reserva.")
    fecha_fin = models.DateField(help_text="Fecha de fin de la reserva.")
    creada_en = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación de la reserva.")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.cabana} del {self.fecha_inicio} al {self.fecha_fin}"