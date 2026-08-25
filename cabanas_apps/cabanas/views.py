""" views"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cabana

# Listado de cabañas
class CabanaListView(ListView):
    model = Cabana
    template_name = "cabanas/cabana_list.html"
    context_object_name = "cabanas"

# Detalle de una cabaña
class CabanaDetailView(DetailView):
    model = Cabana
    template_name = "cabanas/cabana_detail.html"
    context_object_name = "cabana"

# Crear nueva cabaña
class CabanaCreateView(CreateView):
    model = Cabana
    template_name = "cabanas/cabana_form.html"
    fields = ["nombre", "descripcion", "precio", "disponible"]
    success_url = reverse_lazy("cabanas:cabanas_list")

# Editar cabaña existente
class CabanaUpdateView(UpdateView):
    model = Cabana
    template_name = "cabanas/cabana_form.html"
    fields = ["nombre", "descripcion", "precio", "disponible"]
    success_url = reverse_lazy("cabanas:cabanas_list")

# Eliminar cabaña
class CabanaDeleteView(DeleteView):
    model = Cabana
    template_name = "cabanas/cabana_confirm_delete.html"
    success_url = reverse_lazy("cabanas:cabanas_list")
