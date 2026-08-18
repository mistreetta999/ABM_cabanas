"""módulo de vistas para la aplicación de gestión de Cabanas."""
from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    """Muestra la lista de clientes."""
    clientes = Cliente.objects.all()
    return render(request, "clientes/lista.html", {"clientes": clientes})
