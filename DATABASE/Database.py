# cabanas_project/DATABASE/database.py
"""Este módulo define la clase Database y las funciones para configurar la base de datos.
La clase Database representa la estructura de la base de datos, mientras que las funciones
get_sqlite_config, get_postgresql_config y get_database_settings proporcionan la configuración necesaria para conectar con la base de datos según el entorno (desarrollo o producción).
"""

import os
from pathlib import Path
from cabana_apps.models import models
from django.db import models
from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models   import CharField

class Database:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.nombre = CharField(max_length=100)
        self.descripcion = CharField(max_length=255)    
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
    Modelo para representar a un cliente en el sistema de gestión de cabañas.
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
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
class Reserva(models.Model):
    """
    Modelo para representar una reserva de cabaña.
    """
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'), 
    ], default='pendiente')     
    def __str__(self):
        return f"Reserva {self.id} - Cliente: {self.cliente.nombre} {self.cliente.apellido} - Estado: {self.estado}"    
    
class Alquiler(models.Model):
    """Modelo para representar un alquiler de cabaña."""
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='alquileres')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    def __str__(self):
        return f"Alquiler {self.id} - Cliente: {self.cliente.nombre} {self.cliente.apellido}"