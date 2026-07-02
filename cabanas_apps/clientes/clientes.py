""" archivo clientes"""
import os
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from django.db import models


class Cliente(models.Model):
    """ Modelo que representa un cliente."""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"





def listar_clientes(request):
    """Muestra todos los clientes registrados."""
    clientes = Cliente.objects.all()
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


def borrar_cliente(request, cliente_id):
    """Elimina un cliente existente."""
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == "POST":
        cliente.delete()
        return redirect("listar_clientes")

    return render(request, "pagina_principal/confirma_borrar.html", {"cliente": cliente})
