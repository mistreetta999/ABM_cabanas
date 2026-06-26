# cabanas/views.py

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from cabanas_apps.models import CabanaListView
from .models import Cabana, Reserva, Alquiler, Cliente, Pago, 


# Vista para listar cabañas
class CabanaListView(ListView):
    model = Cabana
    template_name = "cabanas/formulario_cabanaListView.html"
    context_object_name = "cabanas"


# Vista para crear reservas
class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    template_name = "cabanas/formulario_reservas.html"
    fields = ["cabana", "fecha_inicio", "fecha_fin", "estado"]
    success_url = reverse_lazy("cabana_list")


# Vista para crear alquileres
class AlquilerCreateView(LoginRequiredMixin, CreateView):
    model = Alquiler
    template_name = "cabanas/formulario_alquileres.html"
    fields = ["reserva", "fecha_inicio", "fecha_fin", "precio_total"]
    success_url = reverse_lazy("cabana_list")


# Vista para crear clientes
class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "cabanas/formulario_clientes.html"
    fields = ["nombre", "apellido", "dni", "direccion", "telefono"]
    success_url = reverse_lazy("cabana_list")


# Vista para crear pagos
class PagoCreateView(LoginRequiredMixin, CreateView):
    model = Pago
    template_name = "cabanas/formulario_pagos.html"
    fields = ["factura", "monto", "metodo"]
    success_url = reverse_lazy("cabana_list")


# Vista para crear facturas
class FacturaCreateView(LoginRequiredMixin, CreateView):
    model = Factura
    template_name = "cabanas/formulario_facturas.html"
    fields = ["alquiler", "monto_total"]
    success_url = reverse_lazy("cabana_list")


# Vista del chatbot
def chatbot_view(request):
    return render(request, "chatbot/chat.html")
