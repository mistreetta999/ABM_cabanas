"""
Vistas para la instancia django_local.
Incluye dashboard, resumen y CRUD de clientes, reservas, facturas, pagos y registros.
"""

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Reserva, Factura, Pago, Registro


class DashboardView(TemplateView):
    """Vista principal del panel de gestión."""
    template_name = "django_local/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_clientes"] = Cliente.objects.count()
        context["total_reservas"] = Reserva.objects.count()
        context["total_facturas"] = Factura.objects.count()
        context["total_pagos"] = Pago.objects.count()
        return context


def resumen(request):
    """Vista rápida con métricas del sistema."""
    data = {
        "clientes": Cliente.objects.count(),
        "reservas": Reserva.objects.count(),
        "facturas": Factura.objects.count(),
        "pagos": Pago.objects.count(),
    }
    return render(request, "django_local/resumen.html", data)


# --- CRUD de Clientes ---
class ClienteListView(ListView):
    model = Cliente
    template_name = "django_local/clientes/list.html"


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "django_local/clientes/detail.html"


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "telefono"]
    template_name = "django_local/clientes/form.html"
    success_url = reverse_lazy("django_local:cliente_list")


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "telefono"]
    template_name = "django_local/clientes/form.html"
    success_url = reverse_lazy("django_local:cliente_list")


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "django_local/clientes/confirm_delete.html"
    success_url = reverse_lazy("django_local:cliente_list")


# --- CRUD de Reservas ---
class ReservaListView(ListView):
    model = Reserva
    template_name = "django_local/reservas/list.html"


class ReservaDetailView(DetailView):
    model = Reserva
    template_name = "django_local/reservas/detail.html"


class ReservaCreateView(CreateView):
    model = Reserva
    fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "monto_total", "estado"]
    template_name = "django_local/reservas/form.html"
    success_url = reverse_lazy("django_local:reserva_list")


class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "monto_total", "estado"]
    template_name = "django_local/reservas/form.html"
    success_url = reverse_lazy("django_local:reserva_list")


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = "django_local/reservas/confirm_delete.html"
    success_url = reverse_lazy("django_local:reserva_list")


# --- Facturas ---
class FacturaListView(ListView):
    model = Factura
    template_name = "django_local/facturas/list.html"


class FacturaDetailView(DetailView):
    model = Factura
    template_name = "django_local/facturas/detail.html"


# --- Pagos ---
class PagoListView(ListView):
    model = Pago
    template_name = "django_local/pagos/list.html"


class PagoDetailView(DetailView):
    model = Pago
    template_name = "django_local/pagos/detail.html"


# --- Registros ---
class RegistroListView(ListView):
    model = Registro
    template_name = "django_local/registros/list.html"
    ordering = ["-fecha"]
