from django.views.generic import ListView, DetailView
from .models import Alquileres, Cabana, Clientes

class CabanaListView(ListView):
    model = Cabana
    template_name = "cabanas/lista.html"
    context_object_name = "cabanas"

class CabanaDetailView(DetailView):
    model = Cabana
    template_name = "cabanas/detalle.html"
    context_object_name = "cabana"

class ClientesListView(ListView):
    model = Clientes
    template_name = "clientes/lista.html"
    context_object_name = "clientes"

class ClientesDetailView(DetailView):
    model = Clientes
    template_name = "clientes/detalle.html"
    context_object_name = "cliente" \
class AlquileresListView(ListView):
    model = Alquileres
    template_name = "alquileres/lista.html" 
    context_object_name = "alquileres"
    
    def get_context_data(self, **kwargs):
        context = super(CLASS_NAME, self).get_context_data(**kwargs)
        return context
    
    ""

class ReservasListView(ListView):
    model = Alquileres
    template_name = "alquileres/lista.html" 
    context_object_name = "reservas"
    
    def get_context_data(self, **kwargs):
        context = super(CLASS_NAME, self).get_context_data(**kwargs)
        return context
    
    ""