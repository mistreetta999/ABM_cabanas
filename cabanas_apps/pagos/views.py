""" archivo de vistas de la app pagos

"""

from django.views.generic import ListView
from .models import Pago

class PagoListView(ListView):
    """ Vista para listar los pagos """
    model = Pago
    template_name = "pagos/list.html"
    context_object_name = "pagos"
