"""models pago"""

from django.db import models

class Pago(models.Model):
    """class Pago(models.Model): Representa un pago realizado para un alquiler de cabaña."""
    METODO_CHOICES = [
        ("EF", "Efectivo"),
        ("TJ", "Tarjeta"),
        ("TR", "Transferencia"),
    ]

    alquiler = models.ForeignKey("reservas.Reserva", on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=2, choices=METODO_CHOICES)
    objects = models.Manager()
    @property
    def metodo_display(self):
        """Devuelve el nombre legible del método de pago."""
        if not self.metodo:
            return ""
        for value, label in self.METODO_CHOICES:
            if value == self.metodo:
                return label
        return self.metodo

    def __str__(self):
        return f"{self.alquiler} - {self.metodo_display} - {self.monto}"
