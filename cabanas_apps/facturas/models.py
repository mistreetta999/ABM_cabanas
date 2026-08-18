from django.db import models
from clientes.models import Cliente

class Factura(models.Model):
    """class factura"""
    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """class meta"""
        verbose_name = "Factura"

    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"
class FacturaCrear(models.Model):
    """class factura crear"""
    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"
class FacturaBorrar(models.Model):
    """"class factura borrar"""
    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"
class FacturaImprimir(models.Model):
    """class imprimir"""
    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"


class FacturaGuardar(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"