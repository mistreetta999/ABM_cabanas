"""
Vistas para la aplicación de facturas.
"""

from cabanas_apps_django.facturas.models import Factura
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


class FacturaListView(ListView):
    """class facturas vistas"""

    model = Factura
    template_name = "facturas/factura_list.html"


class FacturaDetailView(DetailView):
    """class factura detalle"""

    model = Factura
    template_name = "facturas/factura_detail.html"


class FacturaCreateView(CreateView):
    """class facturas crear"""

    model = Factura
    fields = ["numero", "cliente", "fecha", "monto_total"]
    template_name = "facturas/factura_form.html"
    success_url = reverse_lazy("facturas:factura_list")


class FacturaUpdateView(UpdateView):
    """class factura vistas"""

    model = Factura
    fields = ["numero", "cliente", "fecha", "monto_total"]
    template_name = "facturas/factura_form.html"
    success_url = reverse_lazy("facturas:factura_list")


class FacturaDeleteView(DeleteView):
    """class facturas borrar"""

    model = Factura
    template_name = "facturas/factura_confirm_delete.html"
    success_url = reverse_lazy("facturas:factura_list")
