""" este archivo es models de reserva. """
from django.db import models
from cabanas_apps.clientes.models import Cliente


class Reserva(models.Model):
    """Modelo que representa una reserva de Cabanas"""
    class Estado(models.TextChoices):
        """Estados posibles de una reserva."""
        PENDIENTE = "pendiente", "Pendiente"
        CONFIRMADA = "confirmada", "Confirmada"
        CANCELADA = "cancelada", "Cancelada"
        COMPLETADA = "completada", "Completada"

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Cabanas= models.ForeignKey('cabanas.Cabanas', on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    ActividadCabana = models.ForeignKey('cabanas.Cabanas',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reservas_actividad',
    )
    objects = models.Manager()

    class Meta:
        """ nombres de la tabla y ordenamiento de la tabla """
        db_table = 'reservas_reserva'
        managed = True
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['fecha_inicio']

    @staticmethod
    def get_reservas_by_cliente(cliente_id):
        """Obtiene todas las reservas de un cliente específico."""
        return Reserva.objects.filter(cliente_id=cliente_id)

    @staticmethod
    def get_reservas_by_cabana(cabana_id):
        """Obtiene todas las reservas de una Cabanas
 específica."""
        return Reserva.objects.filter(cabana_id=cabana_id)

    @staticmethod
    def get_all_reservas():
        """Obtiene todas las reservas."""
        return Reserva.objects.all()

    def get_actividad_cabana(self):
        """Obtiene la actividad asociada a la reserva."""
        return self.ActividadCabana

    def __str__(self)-> str:
        return f"Reserva {self.cliente} - {self.Cabanas}  - Estado: {self.estado}"
