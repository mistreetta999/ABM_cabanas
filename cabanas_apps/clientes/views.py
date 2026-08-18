""" views - Definición de las vistas para la aplicación de clientes. """

from typing import Any

from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse ,HttpRequest
from .models import Cliente, Pago, Factura

class ClienetesViews(ListView):
    """Vista para listar todos los clientes registrados en la aplicación."""
    model = Cliente
    template_name = "clientes/panel.html"
    context_object_name = "clientes"
class ClientesListaPagosView(ListView):
    """Vista para listar todos los pagos realizados por los clientes."""
    model = Pago
    template_name = "clientes/lista_pagos.html"
    context_object_name = "pagos"

class ClientesListaFacturasView(ListView):
    """Vista para listar todas las facturas de los clientes."""
    model = Factura
    template_name = "clientes/lista_facturas.html"
    context_object_name = "facturas"

# Vista basada en clase para listar clientes
class ClienteListView(ListView):
    """Vista para listar todos los clientes registrados en la aplicación."""
    model = Cliente
    template_name = "clientes/panel.html"
    context_object_name = "clientes"
def lista_clientes(_request):
    """Vista Django para mostrar la lista de clientes."""
    return ClienteListView.as_view()(_request)

# Vista para detalle de un cliente
class ClienteDetailView(DetailView):
    """Vista para mostrar los detalles de un cliente específico."""             
    model = Cliente
    template_name = "clientes/detalle_cliente.html"
    context_object_name = "cliente"

# Vista para crear un cliente
class ClienteCreateView(CreateView):
    """Vista para crear un nuevo cliente en la aplicación."""
    model = Cliente
    template_name = "clientes/form_cliente.html"
    fields = ["nombre", "apellido", "dni", "direccion", "telefono", "email"]
    success_url = reverse_lazy("clientes:lista")

# Vista para actualizar un cliente

class ClienteUpdateView(UpdateView):
    """Vista para actualizar la información de un cliente existente."""
    model = Cliente
    template_name = "clientes/form_cliente.html"
    fields = ["nombre", "apellido", "dni", "direccion", "telefono", "email"     ]
    success_url = reverse_lazy("clientes:lista")

# Vista para eliminar un cliente
class ClienteDeleteView(DeleteView):
    """Vista para eliminar un cliente de la aplicación."""
    model = Cliente
    template_name = "clientes/confirmar_eliminar.html"
    success_url = reverse_lazy("clientes:lista")
class PagoListView(ListView):
    """Vista para listar todos los pagos realizados por los clientes."""
    model = Pago
    template_name = "clientes/lista_pagos.html"
    context_object_name = "pagos"
class ClientesTemplateView(TemplateView):
    """Vista para mostrar la plantilla de la aplicación."""
    template_name = "clientes/template.html"

class ClientesHomeView(TemplateView):
    """Vista para la página de pagina_principal de la sección de clientes."""
    template_name = "clientes/panel.html"

def admin_clientes(request: HttpRequest) -> HttpResponse:
    """Vista para el panel de administración de clientes."""
    return HttpResponse("Panel de administración de clientes")
class CabanasBotonesViews(View):
    # Añade el método a la lista de columnas visibles
    list_display = ('id', 'nombre', 'botones_crud_cabanas')

    def ClienteBotonVews(self, obj)->Any:
        """"vistes de botones clientes crud"""
        editar = reverse('editar:app_mimodelo_change', args=[obj.pk])
        eliminar = reverse('eliminar:app_mimodelo_delete', args=[obj.pk])
        crear = reverse('crear:app_mimodelo_create', args=[obj.pk])
        imprimir = reverse('imprimir:app_mimodelo_print', args=[obj.pk])
        buscar = reverse('buscar:app_mimodelo_find', args=[obj.pk])
        salir = reverse('buscar:app_mimodelo_exit', args=[obj.pk])
        return {
            "editar": editar,
            "eliminar": eliminar,
            "crear": crear,
            "imprimir": imprimir,
            "buscar": buscar,
            "salir": salir,
        }
