# cabanas_apps/alquileres/models.py

from logging import getLogger
from typing import Any

from django.db import models

# Importar modelos de otras apps
from cabanas_apps.cabanas.models import Cabanas

from cabanas_apps.clientes.models import Cliente
from cabanas_apps.reservas.models import Reserva

LOGGER = getLogger(__name__)


class Alquiler(models.Model):
    """Modelo Alquiler."""

    id = models.AutoField(primary_key=True)
    cabanas = models.ForeignKey(Cabanas
, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reservas = models.OneToOneField(
        Reserva,
        on_delete=models.CASCADE,
        db_column="reserva_id",
    )
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquileres"

    def __str__(self) -> str:
        return f"Alquiler {self.id} - {self.reservas}"

    def actualizar(self, **datos: Any) -> "Alquiler":
        for campo, valor in datos.items():
            setattr(self, campo, valor)
        self.save(update_fields=list(datos.keys()) if datos else None)
        return self

    def eliminar(self):
        return self.delete()


class AlquilerManager(models.Manager):
    """Manager con operaciones para Alquiler."""

    def crear(self, **datos: Any) -> "Alquiler":
        LOGGER.info("Creando alquiler")
        return self.create(**datos)

    def listar(self, **filtros: Any):
        consulta = self.get_queryset()
        return consulta.filter(**filtros) if filtros else consulta

    def obtener(self, alquiler_id: Any) -> "Alquiler":
        return self.get(pk=alquiler_id)

    def actualizar(self, alquiler_id: Any, **datos: Any) -> "Alquiler":
        alquiler = self.obtener(alquiler_id)
        for campo, valor in datos.items():
            setattr(alquiler, campo, valor)
        alquiler.save(update_fields=list(datos.keys()) if datos else None)
        LOGGER.info("Alquiler %s actualizado", alquiler_id)
        return alquiler

    def eliminar(self, alquiler_id: Any):
        alquiler = self.obtener(alquiler_id)
        LOGGER.info("Eliminando alquiler %s", alquiler_id)
        return alquiler.delete()
