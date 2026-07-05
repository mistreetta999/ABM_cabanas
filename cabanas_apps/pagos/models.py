class Pago(models.Model):
    """ Modelo que representa un pago de un alquiler """
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE, related_name="pagos")
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=30)
    comprobante = models.CharField(max_length=200, blank=True)
    class Meta:
        """ class Meta para definir el nombre del modelo en singular y plural. """  
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    def __str__(self):
        return f"Pago {self.pk}"
