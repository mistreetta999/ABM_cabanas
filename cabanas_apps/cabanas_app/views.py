from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cabana
from .forms import CabanaForm

# Listar todas las cabañas
class CabanaListView(ListView):
    """ cabanas views"""
    model = Cabana
    context_object_name = "cabanas"

# Ver detalle de una cabaña
class CabanaDetailView(DetailView):
    """ cabanas detalle """
    model = Cabana
    context_object_name = "cabana"

# Crear nueva cabaña (devuelve form de Django)
class CabanaCreateView(CreateView):
    """ cabana crear """
    model = Cabana
    form_class = CabanaForm
    success_url = reverse_lazy("cabanas_app:cabana_list")

# Editar cabaña existente (devuelve form de Django)
class CabanaUpdateView(UpdateView):
    """cabana actualizar"""
    model = Cabana
    form_class = CabanaForm
    success_url = reverse_lazy("cabanas_app:cabana_list")

# Eliminar cabaña
class CabanaDeleteView(DeleteView):
    """"borrar """
    model = Cabana
    success_url = reverse_lazy("cabanas_app:cabana_list")
