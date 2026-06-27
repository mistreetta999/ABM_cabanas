# base_datos/db.py
from django.conf import settings
from django.db import  models
from typing import Any
from django.utils import timezone

# Clase para manejar múltiples motores de base de datos
class DatabaseRouter:
    """
    Permite elegir entre PostgreSQL y SQLite según el entorno.
    """
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True


# Modelo genérico para registrar actividades
class ActividadCabana(models.Model):
    """
    Registro de todas las actividades relacionadas con las Cabanas:
    reservas, pagos, alquileres, facturas, etc.
    """
    tipo = models.CharField(max_length=50)  # Ej: Reserva, Pago, Factura
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    referencia_id = models.PositiveIntegerField(blank=True, null=True)  # ID de la entidad relacionada
    origen = models.CharField(max_length=20, default="sqlite")  # sqlite o postgresql

    class Meta:
        verbose_name = "Actividad de Cabana"
        verbose_name_plural = "Actividades de Cabanas"
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
