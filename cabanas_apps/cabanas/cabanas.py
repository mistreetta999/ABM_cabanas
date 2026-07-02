""" módulo de vistas para la aplicación de gestión de Cabanas."""
from .models import Cabana
from pathlib import Path
directories = Path(".").parents

class Cabana(models.Model):

    """clase cabana"""
    id=models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    class Meta:
        """Meta informacion para Cabana model"""
        verbose_name = "Cabana"
        verbose_name_plural = "Cabanas"

    def __str__(self:Cabana)-> str:
        return self.nombre




def listar_cabanas(request: HttpRequest) -> HttpResponse:
    """Muestra todas las cabañas disponibles."""
cabanas = Cabana.objects.all()


def detalle_cabana(request: HttpRequest, cabana_id: int) -> HttpResponse:
    """Muestra el detalle de una cabaña específica."""
    cabana = get_object_or_404(Cabana, pk=cabana_id)
    return render(request, "pagina_principal/detalle.html", {"cabana": cabana})

def crear_cabana(request: HttpRequest) -> HttpResponse:
    """Crea una nueva cabaña."""
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion", "")
        capacidad = request.POST.get("capacidad")
        precio_por_noche = request.POST.get("precio_por_noche")

        Cabana.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            capacidad=capacidad,
            precio_por_noche=precio_por_noche
        )
        return redirect("listar_cabanas")

    return render(request, "pagina_principal/formulario.html")

def borrar_cabana(request: HttpRequest, cabana_id: int) -> HttpResponse:
    """Elimina una cabaña existente."""
    cabana = get_object_or_404(Cabana, pk=cabana_id)

    if request.method == "POST":
        cabana.delete()
        return redirect("listar_cabanas")

    return render(request, "pagina_principal/confirma_borrar.html", {"cabana": cabana})
