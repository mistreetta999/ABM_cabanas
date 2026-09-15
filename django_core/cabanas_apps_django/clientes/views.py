"""views - Definición de las vistas para la aplicación de clientes."""

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Cliente


# Vista basada en clase para listar clientes
class ClienteListView(ListView):
    """Listado de clientes."""

    model = Cliente
    template_name = "clientes/lista_clientes.html"
    context_object_name = "clientes"


# Vista para detalle de un cliente
class ClienteDetailView(DetailView):
    """Detalle de un cliente específico."""

    model = Cliente
    template_name = "clientes/detalle_cliente.html"
    context_object_name = "cliente"


# Vista para crear un cliente
class ClienteCreateView(CreateView):
    """Vista para crear un cliente."""

    model = Cliente
    template_name = "clientes/form_cliente.html"
    fields = ["nombre", "email", "telefono"]
    success_url = reverse_lazy("clientes:lista")


# Vista para actualizar un cliente
class ClienteUpdateView(UpdateView):
    """Vista para actualizar un cliente."""

    model = Cliente
    template_name = "clientes/form_cliente.html"
    fields = ["nombre", "email", "telefono"]
    success_url = reverse_lazy("clientes:lista")


# Vista para eliminar un cliente
class ClienteDeleteView(DeleteView):
    """Vista para eliminar un cliente."""

    model = Cliente
    template_name = "clientes/confirmar_eliminar.html"
    success_url = reverse_lazy("clientes:lista")


class ClienteHomeView(DetailView):
    """Vista para el home de un cliente específico."""

    model = Cliente
    template_name = "clientes/home_cliente.html"
    context_object_name = "cliente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí puedes agregar cualquier contexto adicional que necesites para el home del cliente
        return context


class ClienteFacturaViews(DetailView):
    """Vista para las facturas de un cliente específico."""

    model = Cliente
    template_name = "clientes/facturas_cliente.html"
    context_object_name = "cliente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí puedes agregar cualquier contexto adicional que necesites para las facturas del cliente
        return context


# Vista simple para el home de clientes
def clientes_home(request):
    """Vista para el home de clientes."""
    return render(request, "clientes/home.html")
