""" archivo clientes"""
import os
from typing import TYPE_CHECKING
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente

class Cliente:
    """Modelo de cliente."""
    def __init__(self, nombre: str, apellido: str, email: str, telefono: str):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.id = None  # Se asignará un ID único al guardar en la base de datos
        self.pagos = []  # Lista de pagos asociados al cliente

if TYPE_CHECKING:
    from django.db.models import QuerySet
def lista_facturas(request):
    # lógica de la vista
    return render(request, 'facturas/lista.html')



def listar_clientes(request):
    """Muestra todos los clientes registrados."""
    clientes: "QuerySet[Cliente]" = Cliente.objects.all()  # pylint: disable=no-member
    return render(request, "pagina_principal/lista.html", {"clientes": clientes})

def detalle_cliente(request, cliente_id):
    """Muestra el detalle de un cliente específico."""
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, "pagina_principal/detalle.html", {"cliente": cliente})

def crear_cliente(request):
    """Crea un nuevo cliente."""
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )
        return redirect("listar_clientes")
    
    return render(request, "pagina_principal/crear_cliente.html")


def borrar_cliente(request, cliente_id):
    """Elimina un cliente existente."""
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == "POST":
        cliente.delete()
        return redirect("listar_clientes")

    return render(request, "pagina_principal/confirma_borrar.html", {"cliente": cliente})
