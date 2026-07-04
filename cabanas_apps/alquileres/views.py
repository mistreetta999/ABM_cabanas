"""Views for the reservas_alquileres_apps application.
"""
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Reserva, Alquiler

from django.shortcuts import render, redirect
from .forms import ReservaForm

def crear_alquileres(request):
    """" Vista para crear un nuevo alquiler """
    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alquileres')
    else:
        form = AlquilerForm()
    return render(request, 'alquileres/crear.html', {'form': form})


def reservas_list(request):
    """ Vista para listar las reservas """
    reservas = Reserva.objects.all()
    return render(request, "reservas_alquileres/reservas_list.html", {"reservas": reservas})

def alquileres_list(request):
    """ Vista para listar los alquileres """
    return AlquilerListView.as_view()(request)

class AlquilerListView(ListView):
    """ Vista para listar las alquileres """
    model = Reserva
    template_name = "reservas_alquileres/reservas_list.html"
    context_object_name = "alquileres"
class AlquilerListView(ListView):
    """ Vista para listar los alquileres """
    model = Alquiler
    template_name = "alquileres_alquileres/alquileres_list.html"
    context_object_name = "alquileres"
class AlquilerCreateView(CreateView):
    """ Vista para crear una nueva reserva """
    model = Reserva
    template_name = "reservas_alquileres/reserva_form.html"
    fields = "__all__"
    success_url = reverse_lazy("reservas_list")
class AlquilerCreateView(CreateView):
    """ Vista para crear un nuevo alquiler """
    model = Alquiler
    template_name = "reservas_alquileres/alquiler_form.html"
    fields = "__all__"
    success_url = reverse_lazy("alquileres_list")
class AlquileresUpdateView(UpdateView):
    """ Vista para actualizar una reserva existente """
    model = Alquiler
    template_name = "reservas_alquileres/reserva_form.html"
    fields = "__all__"
    success_url = reverse_lazy("reservas_list")
class AlquilerUpdateView(UpdateView):
    """ Vista para actualizar un alquiler existente """
    model = Alquiler
    template_name = "reservas_alquileres/alquiler_form.html"
    fields = "__all__"
    success_url = reverse_lazy("alquileres_list")
    