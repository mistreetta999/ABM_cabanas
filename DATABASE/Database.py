# cabanas_project/DATABASE/database.py
"""Este módulo define la clase Database y las funciones para configurar la base de datos."""

import os
from pathlib import Path

from cabanas_apps.models import models

class Database:
    """ Clase que representa la configuración de la base de datos para el proyecto de gestión de Cabanas."""
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent
        self.nombre = models.CharField(max_length=100)
        self.descripcion = models.CharField(max_length=255)    
        self.reservas = models.ManyToManyField('Reserva', related_name='cabanas')
        self.alquileres = models.ManyToManyField('Alquiler', related_name='cabanas')    
        self.precios = models.ManyToManyField('Precio', related_name='cabanas')
        self.registros = models.ManyToManyField('Registro', related_name='cabanas')
    

BASE_DIR = Path(__file__).resolve().parent.parent

def get_sqlite_config():
    """
    Configuración para SQLite3 (desarrollo/local).
    """
    return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

def get_postgresql_config():
    """
    Configuración para PostgreSQL (producción).
    Usa variables de entorno para mayor seguridad.
    """
    return {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', 'cabanas_db'),
            'USER': os.getenv('POSTGRES_USER', 'postgres'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
            'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
            'PORT': os.getenv('POSTGRES_PORT', '5432'),
        }
    }

def get_database_settings():
    """
    Retorna la configuración según el entorno.
    Usa la variable de entorno DJANGO_ENV para decidir.
    """
    env = os.getenv('DJANGO_ENV', 'development')

    if env == 'production':
        return get_postgresql_config()
    else:
        return get_sqlite_config()
    
class Cliente(models.Model):
    """
    Modelo para representar a un cliente en el sistema de gestión de Cabanas.
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    registros = models.ManyToManyField('Registro', related_name='cabanas')
    
    dni = models.CharField(
        max_length=20,       # máximo 20 caracteres
        unique=True,         # no se repite
        blank=False,         # obligatorio en formularios
        null=False           # obligatorio en base de datos
    )
 

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"
    class Meta:
        """Meta información para el modelo Cliente."""
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
class Reserva(models.Model):
    """
    Modelo para representar una reserva de Cabana.
    """
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    nombre = models.CharField(max_length=100)   
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'), 
    ], default='pendiente')     
    def __str__(self)-> str:
        return f"Reserva {self.id} - Cliente: {self.cliente} - Estado: {self.estado}"    
    
class Alquiler(models.Model):
    """Modelo para representar un alquiler de Cabana."""
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='alquileres')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    def __str__(self)-> str:
        return f"Alquiler {self.id} - Cliente: {self.cliente}"