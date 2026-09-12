""" models """
from django.db import models
from django_core.cabanas_apps_django.alquileres.models import Alquiler, Cliente


class Factura(models.Model):
    """ facturas"""
    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    cabana = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="facturas")
    fecha_emision = models.DateField(auto_now_add=True)
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="facturas")
    reserva = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="facturas")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    pagos = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """ Metadatos de la clase Factura """
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"


class DetalleFactura(models.Model):
    """ detalles de facturas"""
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="detalles")
    descripcion = models.CharField(max_length=200)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total_linea = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """ Metadatos de la clase DetalleFactura """
        verbose_name = "Detalle de Factura"
        verbose_name_plural = "Detalles de Factura"

    def __str__(self):
        return f"{self.descripcion} ({self.cantidad} x {self.precio_unitario})"
