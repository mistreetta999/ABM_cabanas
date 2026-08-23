""" views - Definición de las vistas para la aplicación de clientes. """
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

# Vista basada en clase para listar clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/lista_clientes.html"
    context_object_name = "clientes"

# Vista para detalle de un cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "clientes/detalle_cliente.html"
    context_object_name = "cliente"

# Vista para crear un cliente
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "clientes/form_cliente.html"
    fields = ["nombre", "email", "telefono"]
    success_url = reverse_lazy("clientes:lista")

# Vista para actualizar un cliente
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "clientes/form_cliente.html"
    fields = ["nombre", "email", "telefono"]
    success_url = reverse_lazy("clientes:lista")

# Vista para eliminar un cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/confirmar_eliminar.html"
    success_url = reverse_lazy("clientes:lista")

# Vista simple para el home de clientes
def clientes_home(request):
    return render(request, "clientes/home.html")
