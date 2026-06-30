""" archivo de base de datos para registrar actividades de cabañas """
from django.db import models
from django.utils import timezone
from django.conf import settings
from .cabanas import Cabanas
from .clientes import Clientes

class ActividadCabana(models.Model):
    """ Modelo para registrar actividades relacionadas con cabañas pagos  """
    tipo = models.CharField(max_length=50)  # Ej: Reserva, Pago, Factura
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    referencia_id = models.PositiveIntegerField(blank=True, null=True)
    origen = models.CharField(max_length=20, default="sqlite")
    reservas = models.ManyToManyField(Cabanas, blank=True)
    alquileres = models.ManyToManyField(Cabanas, blank=True)
    facturas = models.ManyToManyField(Cabanas, blank=True)
    pagos = models.ManyToManyField(Cabanas, blank=True)
    clientes = models.ManyToManyField(Cabanas, blank=True)

    class Meta:
        
        """ Meta options for the ActividadCabana model. """
        verbose_name = "Actividad de Cabaña"
        verbose_name_plural = "Actividades de Cabañas"
        ordering = ["-fecha"]

    def __str__(self):
        return f"[{self.tipo}] {self.descripcion} ({self.fecha})"

    @staticmethod
    def registrar_actividad(
        tipo: str,
        descripcion: str,
        referencia_id: int | None = None
    ):
        """ Función para registrar una actividad de cabaña en la base de datos. """
        engine = settings.DATABASES['default']['ENGINE']
        origen = "postgresql" if "postgresql" in engine else "sqlite"

        actividad = ActividadCabana(
            tipo=tipo,
            descripcion=descripcion,
            referencia_id=referencia_id,
            origen=origen
        )
        actividad.save()
        return actividad
