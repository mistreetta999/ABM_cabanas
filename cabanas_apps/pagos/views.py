"""
Vistas de la aplicación Pagos.
Permite gestionar pagos vinculados a facturas y clientes.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pago
from facturas.models import Factura


class PagoListView(ListView):
    """Lista todos los pagos registrados."""
    model = Pago
    template_name = "pagos/pago_list.html"
    context_object_name = "pagos"


class PagoDetailView(DetailView):
    """Muestra el detalle de un pago."""
    model = Pago
    template_name = "pagos/pago_detail.html"
    context_object_name = "pago"


class PagoCreateView(CreateView):
    """Permite registrar un nuevo pago."""
    model = Pago
    template_name = "pagos/pago_form.html"
    fields = ["factura", "cliente", "monto", "metodo", "referencia"]
    success_url = reverse_lazy("pagos:pago_list")

    def form_valid(self, form):
        # Guardar el pago y marcar la factura como pagada si corresponde
        response = super().form_valid(form)
        self.object.marcar_factura_pagada()
        return response


class PagoUpdateView(UpdateView):
    """Permite editar un pago existente."""
    model = Pago
    template_name = "pagos/pago_form.html"
    fields = ["factura", "cliente", "monto", "metodo", "referencia"]
    success_url = reverse_lazy("pagos:pago_list")


class PagoDeleteView(DeleteView):
    """Permite eliminar un pago."""
    model = Pago
    template_name = "pagos/pago_confirm_delete.html"
    success_url = reverse_lazy("pagos:pago_list")
