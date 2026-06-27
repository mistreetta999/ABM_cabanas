from django.db import models

class Cabana(models.Model):
    """
    Modelo que representa a cada una de las Cabanas del complejo.
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Cabana")
    capacidad_clientes = models.PositiveIntegerField(default=2)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    esta_activa = models.BooleanField(default=True, verbose_name="Disponible para alquilar")

    class Meta:
        verbose_name = "Cabana"
        verbose_name_plural = "Cabanas"

    def __str__(self):
        return f"{self.nombre} (Capacidad: {self.capacidad_clientes})"


class RegistroDiario(models.Model):
    """
    Modelo para el control diario de las Cabanas (novedades, limpieza, mantenimiento).
    """
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="registros_diarios")
    cabana_gestion = models.ForeignKey(
        "cabanas_apps.Cabana",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="registros_diarios",
        verbose_name="Cabana gestion",
    )
    cabana_reservas = models.ForeignKey(
        "reservas.Cabana",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="registros_diarios",
        verbose_name="Cabana reservas",
    )
    reserva_gestion = models.ForeignKey(
        "cabanas_apps.Reserva",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="registros_diarios",
        verbose_name="Reserva gestion",
    )
    reserva = models.ForeignKey(
        "reservas.Reserva",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="registros_diarios",
    )
    fecha = models.DateField(auto_now_add=True)
    novedades = models.TextField(help_text="Ej: Se rompió una lamparita, limpieza realizada, etc.")
    fue_limpiada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Registro Diario"
        verbose_name_plural = "Registros Diarios"

    def __str__(self):
        return f"Registro {self.cabana.nombre} - {self.fecha}"
