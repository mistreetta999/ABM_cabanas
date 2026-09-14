from decimal import Decimal
"""Modelos para la aplicación web de publicaciones."""
from django.db import models
from django.urls import reverse


class Publicacion(models.Model):
    """ publicacio"""
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        """"meta datas"""
        ordering = ["-creado_en"]
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"

    def __str__(self)-> str:
        return str(self.titulo)
def get_absolute_url(self):
        """Devuelve la URL absoluta para la publicación."""
        return reverse("publicacion_detail", kwargs={"pk": self.pk})
    
