"""Views para la aplicación de Cabanas."""
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cabana
from django.shortcuts import render

# Vista inicial
def index(request) -> HttpResponse:
    return HttpResponse("Vista inicial de Cabanas")


def pagina_principal(request):
    return render(request, "pagina_principal.html")


# Vista de lista usando función
def lista_cabanas(request):
    cabanas = Cabana.objects.all()
    return render(request, "cabanas/lista.html", {"cabanas": cabanas})

# Vista basada en clase para listar
class CabanaListView(ListView):
    model = Cabana
    template_name = "cabanas/lista.html"
    context_object_name = "cabanas"

# Vista basada en clase para detalle
class CabanaDetailView(DetailView):
    model = Cabana
    template_name = "cabanas/detalle.html"
    context_object_name = "cabana"

# Vista basada en clase para crear
class CabanaCreateView(CreateView):
    model = Cabana
    template_name = "cabanas/crear.html"
    fields = ["nombre", "descripcion", "precio_base", "capacidad"]

# Vista basada en clase para actualizar
class CabanaUpdateView(UpdateView):
    model = Cabana
    template_name = "cabanas/actualizar.html"
    fields = ["nombre", "descripcion", "precio_base", "capacidad"]

# Vista basada en clase para eliminar
class CabanaDeleteView(DeleteView):
    model = Cabana
    template_name = "cabanas/eliminar.html"
    success_url = "/cabanas/"
