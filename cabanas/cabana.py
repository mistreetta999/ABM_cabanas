"""  archivo cabanas"""
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from .models import Cabana

def Cabana():
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    print("Cabaña creada:", nombre, ubicacion, capacidad, precio_por_noche)



def detalle_cabana(request, cabana_id):
    """Muestra el detalle de una cabaña específica."""
    cabana = get_object_or_404(Cabana, pk=cabana_id)
    return render(request, "pagina_principal/detalle.html", {"cabana": cabana})

def crear_cabana(request):
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

def borrar_cabana(request, cabana_id):
    """Elimina una cabaña existente."""
    cabana = get_object_or_404(Cabana, pk=cabana_id)

    if request.method == "POST":
        cabana.delete()
        return redirect("listar_cabanas")

    return render(request, "pagina_principal/confirma_borrar.html", {"cabana": cabana})
    
def listar_cabanas(request):
    """Muestra todas las cabañas disponibles."""
    cabana.list()
    
    return render(request, "pagina_principal/lista.html", {"cabanas": cabanas})
