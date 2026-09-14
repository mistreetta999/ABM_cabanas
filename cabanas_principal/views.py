"""Vistas de la API de cabañas con class-based views."""

from django.http import JsonResponse
from django.apps import apps
from django.views import View
from django.views.generic import ListView, DetailView
from cabanas_api.models import Alquiler
from cabanas_api.models import Factura
from cabanas_api.models  import Cliente
from cabanas_api.models import Pago
from cabanas_api.models import Registro
class FacturaListView(ListView):
    """Listado de facturas."""
    model = Factura
    template_name = "facturas/list.html"
    context_object_name = "facturas"
class ApiHomeView(View):
    """Vista principal de la API."""
    def get(self, request, *_args, **_kwargs):
        """Devuelve un mensaje de bienvenida en formato JSON."""
        _ = request.method
        return JsonResponse({"message": "Bienvenido a la API de Cabañas"}, status=200)


class AlquilerListView(ListView):
    """Listado de alquileres."""
    model = Alquiler
    template_name = "alquileres/list.html"
    context_object_name = "alquileres"


class AlquilerDetailView(DetailView):
    """Detalle de un alquiler específico."""
    model = Alquiler
    template_name = "alquileres/detail.html"
    context_object_name = "alquiler"


class ClienteListView(ListView):
    """Listado de clientes."""
    model = Cliente
    template_name = "clientes/list.html"
    context_object_name = "clientes"


class PagoListView(ListView):
    """Listado de pagos."""
    model = Pago
    template_name = "pagos/list.html"
    context_object_name = "pagos"

class RegistroListView(ListView):
    """Listado de registros de entrada."""
    model = Registro
    template_name = "registros/list.html"
    context_object_name = "registros"


class CabanaListView(ListView):
    """Listado de cabañas."""
    model = apps.get_model("cabanas_api", "Cabana")
    template_name = "cabanas/list.html"
    context_object_name = "cabanas"
class ClienteViewSet(View):
    """Vista de cliente para la API."""
    def get(self, request, *_args, **_kwargs):
        """Devuelve la lista de clientes en formato JSON."""
        _ = request.method
        clientes = list(Cliente.objects.values())  # pylint: disable=no-member
        return JsonResponse({"clientes": clientes}, status=200)