""" views - Definición de las vistas para la aplicación de clientes. """

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Cliente, Pago, Factura


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
    template_name = "clientes/lista_clientes.html"
    context_object_name = "clientes"
def lista_clientes(_request):
    """Vista para obtener la lista de clientes en formato JSON."""
    models = __import__('cabanas_apps.clientes.models', fromlist=['Cliente'])
    clientes = models.Cliente.objects.all().values("id", "nombre", "apellido")
    return JsonResponse(list(clientes), safe=False)

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
class TemplateView(ListView):
    """Vista para mostrar la plantilla de la aplicación."""
    template_name = "clientes/template.html"

class ClientesHomeView(TemplateView):
    """Vista para la página de inicio de la sección de clientes."""
    template_name = "clientes/home.html"