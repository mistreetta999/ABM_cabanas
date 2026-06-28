""" Archivo de modelos de la app pagos"""
from django.db import models


class Pago(models.Model):
    """ Modelo para representar un pago realizado por un cliente """
    reservas = models.ForeignKey('reservas.Reserva', on_delete=models.CASCADE)
    alquileres = models.ForeignKey('alquileres.Alquiler', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    def __str__(self) -> str:
        """ Representación en cadena del modelo Pago """
        return f"Pago de {self.monto} para {self.alquileres} y {self.reservas} {self.fecha_pago}"
    class Meta:
        """ Meta options for the Pago model """
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
     #   ordering = ['-fecha_pago']   