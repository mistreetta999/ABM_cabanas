""" este archivo es models de reserva. """
from django.db import models
from cabanas_apps.clientes.models import Cliente
from typing import Any

class Reserva(models.Model):
    """Modelo que representa una reserva de Cabana."""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cabana = models.ForeignKey('cabanas.Cabana', on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=20, default="pendiente")
    ActividadCabana = models.ForeignKey('cabanas.ActividadCabana', on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()

    @staticmethod
    def get_reservas_by_cliente(cliente_id):
        """Obtiene todas las reservas de un cliente específico."""
        return Reserva.objects.filter(cliente_id=cliente_id)

    @staticmethod
    def get_reservas_by_cabana(cabana_id):
        """Obtiene todas las reservas de una Cabana específica."""
        return Reserva.objects.filter(cabana_id=cabana_id)

    @staticmethod
    def get_all_reservas():
        """Obtiene todas las reservas."""
        return Reserva.objects.all()
    def ActividadCabana(self)-> Any:
        """Obtiene todas las actividades de una Cabana específica."""
        actividades = ActividadCabana.objects.filter(referencia_id=self.id)
        return actividades

    def __str__(self):
        return f"Reserva {self.cliente} - {self.cabana}  - Estado: {self.estado}"


    
    class Meta:
        """ nombres de la tabla y ordenamiento de la tabla """
        db_table = 'reservas_reserva'
        managed = True
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['fecha_inicio']
        