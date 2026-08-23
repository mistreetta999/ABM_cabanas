""" archivo de modelos para la app de clientes """
from logging import getLogger
from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.db import models

class Usuario(AbstractUser):
    """class usuario"""
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    nro_cliente = models.CharField(max_length=20, unique=True, null=True, blank=True)
    dni = models.CharField(max_length=20, unique=True, null=True, blank=True)
    class Meta:
        """class meta"""
        verbose_name = "Usuario"
         verbose_name_plural = "Usuarios"
    def __str__(self):
        return self.username


class Cliente(models.Model):
    """class meta"""
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="perfil_cliente")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    class Meta:
        """ class meta"""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ClienteDatos(models.Model):
    """ Modelo que representa un cliente """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    dni = models.CharField(
        max_length=20,
        unique=True,          # obligatorio y único, pero no clave primaria
        validators=[RegexValidator(r'^\d{1,20}$', 'El DNI debe contener solo números (máx. 20).')]
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)


    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"

    def actualizar(self, **datos: Any) -> "Cliente":
        """Actualiza la instancia actual."""
        for campo, valor in datos.items():
            setattr(self, campo, valor)
        self.save(update_fields=list(datos.keys()) if datos else None)
        return self

    def eliminar(self):
        """Elimina la instancia actual."""
        return self.delete()
class ClienteManager(models.Manager):
    """Manager con operaciones interfaz_gestion_cabanas para Cliente."""

    def crear(self, **datos: Any) -> "Cliente":
        """Crea un cliente."""
        LOGGER.info("Creando cliente")
        return self.create(**datos)

    def listar(self, **filtros: Any):
        """Lista clientes, opcionalmente filtrados."""
        consulta = self.get_queryset()
        return consulta.filter(**filtros) if filtros else consulta

    def obtener(self, cliente_id: Any) -> "Cliente":
        """Obtiene un cliente por id."""
        return self.get(pk=cliente_id)

    def actualizar(self, cliente_id: Any, **datos: Any) -> "Cliente":
        """Actualiza un cliente por id."""
        cliente = self.obtener(cliente_id)
        for campo, valor in datos.items():
            setattr(cliente, campo, valor)
        cliente.save(update_fields=list(datos.keys()) if datos else None)
        LOGGER.info("Cliente %s actualizado", cliente_id)
        return cliente

    def eliminar(self, cliente_id: Any):
        """Elimina un cliente por id."""
        cliente = self.obtener(cliente_id)
        LOGGER.info("Eliminando cliente %s", cliente_id)
        return cliente.delete()

class UsuarioSistema(models.Model):
    """ Modelo que representa un usuario del sistema """
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField("usuarios.Usuario", on_delete=models.CASCADE)
    # otros campos extra, ej:
    nro_cliente = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return str(self.usuario)


