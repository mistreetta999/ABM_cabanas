from django.db import models

class Pago(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.id} - {self.monto}"
