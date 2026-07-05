""" archivo de modelos para la app de clientes """
from django.db import models
from django.core.validators import RegexValidator


class Cliente(models.Model):
    """ Modelo que representa un cliente """
    id = models.AutoField(primary_key=True)  # clave primaria automática
    dni = models.IntegerField(unique=True, validators=[RegexValidator(r'^\d{8}$', message="DNI")])
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    class Meta:
        """ class meta para el nombre"""
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"
class ListaClientes(models.Model):
    """ Modelo que representa una lista de clientes """
    id = models.AutoField(primary_key=True)
    clientes = models.ManyToManyField(Cliente, related_name="listas_clientes")
    class Meta:
        """ class meta para el nombre"""
        verbose_name = "Lista de Clientes"
        verbose_name_plural = "Listas de Clientes"
    def __str__(self):
        return f"Lista de Clientes {self.id}"
class ClientesPago(models.Model):
    """Modelo que representa un pago de un alquiler."""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"Pago de {self.cliente} por {self.monto}"

class FacturaCliente(models.Model):
    """Modelo que representa una factura de un cliente."""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return f"Factura {self.numero} de {self.cliente}"
class ListaFacturas(models.Model):
    """ Modelo que representa una lista de facturas """
    id = models.AutoField(primary_key=True)
    facturas = models.ManyToManyField(FacturaCliente, related_name="listas_facturas")
    class Meta:
        """ class meta para el nombre"""
        verbose_name = "Lista de Facturas"
        verbose_name_plural = "Listas de Facturas"
    def __str__(self):
        return f"Lista de Facturas {self.id}"