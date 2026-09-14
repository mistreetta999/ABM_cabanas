from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pago

class PagoListView(ListView):
    """Lista todos los pagos"""
    model = Pago
    template_name = "pagos/lista_pagos.html"
    context_object_name = "pagos"
    ordering = ["-fecha"]

class PagoDetailView(DetailView):
    """Detalle de un pago específico"""
    model = Pago
    template_name = "pagos/detalle_pago.html"
    context_object_name = "pago"

class PagoCreateView(CreateView):
    """Crear un nuevo pago"""
    model = Pago
    template_name = "pagos/formulario_pago.html"
    fields = ["alquiler", "fecha", "monto", "metodo", "comprobante"]
    success_url = reverse_lazy("lista_pagos")

class PagoUpdateView(UpdateView):
    """Editar un pago existente"""
    model = Pago
    template_name = "pagos/formulario_pago.html"
    fields = ["alquiler", "fecha", "monto", "metodo", "comprobante"]
    success_url = reverse_lazy("lista_pagos")

class PagoDeleteView(DeleteView):
    """Eliminar un pago"""
    model = Pago
    template_name = "pagos/confirma_borrar.html"
    success_url = reverse_lazy("lista_pagos")
