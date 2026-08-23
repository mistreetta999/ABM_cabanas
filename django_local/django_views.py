from django.views.generic import ListView, DetailView
from .models import Cabanas
,Reserva, Alquileres,Pago,Factura
from .views import CabanaListView, CabanaDetailView
class CabanaListViewLista(ListView):
    model = Cabanas

    template_name = "cabanas/lista.html"
    context_object_name = "cabanas"

class CabanaDetailView(DetailView):
    model = Cabanas

    template_name = "cabanas/Cabanas
.html"
    context_object_name = "Cabanas
"
class AlquileresListView(ListView):
    model = Alquileres
    template_name = "alquileres/lista.html"
    context_object_name = "alquileres"

class AlquileresDetailView(DetailView):
    model = Alquileres
    template_name = "alquileres/alquiler.html"
    context_object_name = "alquiler"
class ReservasListView(ListView):
    model = Reserva
    template_name = "reservas/lista.html"
    context_object_name = "reservas"
class ReservaDetailView(DetailView):
    model = Reserva
    template_name = "reservas/reserva.html"
    context_object_name = "reserva"
class PagoListView(ListView):
    model = Pago
    template_name = "pagos/lista.html"
    context_object_name = "pagos"
class PagoDetailView(DetailView):
    model = Pago
    template_name = "pagos/pago.html"
    context_object_name = "pago"
class FacturaListView(ListView):
    model = Factura
    template_name = "facturas/lista.html"
    context_object_name = "facturas"
class FacturaDetailView(DetailView):
    model = Factura
    template_name = "facturas/factura.html"
    context_object_name = "factura"
    