from django.db import models

class Alquiler(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.ForeignKey("clientes.Cliente", on_delete=models.CASCADE)
    cabana = models.ForeignKey("cabanas.Cabana", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente} - {self.cabana}"
