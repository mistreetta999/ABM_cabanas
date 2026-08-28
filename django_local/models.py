"""
Modelos principales para la instancia django_local.
Definen las entidades clave del sistema de gestión de cabañas.
"""

from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    """Modelo para clientes del sistema."""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cabana(models.Model):
    """Modelo para cabañas disponibles en el sistema."""
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    """Modelo para reservas de cabañas."""
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
        ("finalizada", "Finalizada"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente} ({self.estado})"

    def duracion(self):
        return (self.fecha_fin - self.fecha_inicio).days


class Factura(models.Model):
    """Modelo para facturas generadas a partir de reservas."""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default="pendiente")
    fecha_emision = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Factura {self.id} - {self.cliente}"


class Pago(models.Model):
    """Modelo para pagos asociados a facturas."""
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(max_length=50, default="efectivo")

    def __str__(self):
        return f"Pago {self.id} - {self.factura}"

    def marcar_factura_pagada(self):
        self.factura.estado = "pagada"
        self.factura.save()


class Registro(models.Model):
    """Modelo para auditoría de acciones en el sistema."""
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.SET_NULL, null=True, blank=True)
    factura = models.ForeignKey(Factura, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.fecha}"
