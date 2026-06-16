from django.views.generic import ListView, DetailView
from django.models import Cabana

class CabanaListViewLista(ListView):
    model = Cabana
    template_name = "cabanas/lista.html"
    context_object_name = "cabanas"

class CabanaDetailView(DetailView):
    model = Cabana
    template_name = "cabanas/cabana.html"
    context_object_name = "cabana"
