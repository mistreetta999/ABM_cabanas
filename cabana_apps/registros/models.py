from django.db import models
from cabana_apps.clientes_app.models import Cliente
from cabana_apps.cabanas_app.models import Cabana

class ActividadCabana(models.Model):
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cabana} - {self.descripcion[:30]}"
