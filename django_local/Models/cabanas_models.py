"""cabana models"""
from django.db import models

class Cabana(models.Model):
    """Modelo principal de Cabañas."""

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        """class meta"""
        verbose_name = "Cabaña"
        verbose_name_plural = "Cabañas"
        ordering = ["nombre"]

    def __str__(self)->str:
        return str(self.nombre)

    def actualizar(self, **datos):
        """Actualiza la instancia actual con datos nuevos."""
        for campo, valor in datos.items():
            setattr(self, campo, valor)
        self.save(update_fields=list(datos.keys()) if datos else None)
        return self

    def eliminar(self):
        """Elimina la instancia actual."""
        return self.delete()
