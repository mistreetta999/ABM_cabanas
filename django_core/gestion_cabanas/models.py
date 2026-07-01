from django.db import models

class GestionLog(models.Model):
    usuario = models.CharField(max_length=100)
    accion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.accion} ({self.fecha})"
