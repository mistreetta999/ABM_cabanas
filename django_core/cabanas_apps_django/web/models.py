from django.db import models


class Publicacion(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en"]
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.titulo
