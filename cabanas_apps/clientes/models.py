""" archivo de modelos para la app de clientes """
from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(models.Model):
    """class cliente de las cabanas"""   
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    class Meta:
        """ class meta como se escribe"""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class FacturaClientes(models.Model):
    """class factura cliente"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20, unique=True)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ListaClientes(models.Model):
    """lista """
    id = models.AutoField(primary_key=True)
    clientes = models.ManyToManyField(Cliente, related_name="listas_clientes")

    class Meta:
        """como se escribe"""
        verbose_name = "Lista de Clientes"
        verbose_name_plural = "Listas de Clientes"

    def __str__(self):
        return f"Lista de Clientes {self.id}"

class ClientesPago(models.Model):
    """"class que muestra los pagos de este"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"Pago de {self.cliente} por {self.monto}"

class FacturaCliente(models.Model):
    """class muestra las facturas de este"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return f"Factura {self.numero} de {self.cliente}"

class ListaFacturasClinte(models.Model):
    """ class lista de facturas"""
    id = models.AutoField(primary_key=True)
    facturas = models.ManyToManyField(FacturaCliente, related_name="listas_facturas")

    class Meta:
        """ class meta """
        verbose_name = "Lista de Facturas"
        verbose_name_plural = "Listas de Facturas"

    def __str__(self):
        return f"Lista de Facturas {self.id}"


class UsuarioSistema(AbstractUser):
    """ estos son los usuarios y sus roles por que django confunde usuario y cliente"""
    ROLES = (
        ("transacciones", "Usuario de Transacciones"),
        ("completo", "Usuario Completo"),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default="transacciones")

    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.rol})"
