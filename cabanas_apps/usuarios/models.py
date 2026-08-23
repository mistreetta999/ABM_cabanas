""""multiples usuarios y permisos de uso"""
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserPermisos(models.Model):
    """ class permisos para el sitema
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Guardar la contraseña encriptada
        if not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.username)

class Usuario(AbstractUser):
    """"class usuarios para el sistema"""
    telefono = models.CharField(max_length=20, blank=True)
    name = 'usuarios_app'

    def __str__(self):
        return str(self.username)
