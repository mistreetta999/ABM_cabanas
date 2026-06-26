from django.db import models
from .cabana_models import Cabana
from .clientes_models import Cliente

class Alquiler(models.Model):
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Alquiler {self.id} - {self.cliente.nombre}"
