""" base_datos/db.py"""
from django.conf import settings
from django.db import  models
from typing import Any
from django.utils import timezone
from cabanas_apps.models import Cabaña, Reserva, Pago, Factura, Alquiler    
# Clase para manejar múltiples motores de base de datos
class DatabaseRouter:
    """
    Permite elegir entre PostgreSQL y SQLite según el entorno.
    """
    def db_for_read(self, _model):
        return 'default'

    def db_for_write(self, _model):
        return 'default'

    def allow_relation(self, _obj1, _obj2):
        return True

    def allow_migrate(self, _db, _app_label, **_hints):
        return True


# Modelo genérico para registrar actividades
class ActividadCabana(models.Model):
    """
    Registro de todas las actividades relacionadas con las cabañas:
    reservas, pagos, alquileres, facturas, etc.
    """
    tipo = models.CharField(max_length=50)  # Ej: Reserva, Pago, Factura
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    referencia_id = models.PositiveIntegerField(blank=True, null=True)  # ID de la entidad relacionada
    origen = models.CharField(max_length=20, default="sqlite")  # sqlite o postgresql

    class Meta:
        verbose_name = "Actividad de Cabaña"
        verbose_name_plural = "Actividades de Cabañas"
        ordering = ["-fecha"]

    def __str__(self):
        return f"[{self.tipo}] {self.descripcion} ({self.fecha})"


# Función auxiliar para registrar actividades
def registrar_actividad(tipo: str, descripcion: str, usuario: str = None, referencia_id: int = None):
    """
    Inserta un registro en la tabla ActividadCabana.
    """
    actividad = ActividadCabana(
        tipo=tipo,
        descripcion=descripcion,
        usuario=usuario,
        referencia_id=referencia_id,
        origen=settings.DATABASES['default']['ENGINE']
    )
    actividad.save()
    return actividad
