"""Vistas para la aplicación de cabañas."""

import os
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from typing import TypeVar, Any

class views:
    def __init__(self):
        self.views = CabanaListView.as_view()
        self.views = CabanaDetailView.as_view()
        self.views = CabanaCreateView.as_view()
        self.views = CabanaUpdateView.as_view()
        self.views = CabanaDeleteView.as_view()
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'lista'
        verbose_name_plural = 'listas'
        
        
class lista:
    """Clase que contiene las vistas de la lista de cabañas.""" 
    def __init__(self)->Any:
        self.lista = CabanaListView.as_view()
        self.detalle_cabana = CabanaDetailView.as_view()
        self.crear_cabana = CabanaCreateView.as_view()
        self.editar_cabana = CabanaUpdateView.as_view()
        self.eliminar_cabana = CabanaDeleteView.as_view()
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'lista'
        verbose_name_plural = 'listas'



class CabanaListView(ListView):
    """ vista para listar las cabañas"""
    model = Cabana
    template_name = "cabanas/list.html"
    context_object_name = "cabanas"
   
# Vista basada en clase: detalle de una cabaña
class CabanaDetailView(DetailView):
    """ vista para mostrar el detalle de una cabaña"""
    model = Cabana
    template_name = "cabanas/detail.html"
    context_object_name = "cabana"

# Vista basada en clase: creación de una cabaña
class CabanaCreateView(CreateView):
    """ vista para crear una nueva cabaña"""
    model = Cabana
    template_name = "cabanas/form.html"
    fields = ["nombre", "descripcion", "capacidad", "precio"]
    success_url = reverse_lazy("cabanas:list")

# Vista basada en clase: edición de una cabaña
class CabanaUpdateView(UpdateView):
    """ vista para editar una cabaña existente"""
    model = Cabana
    template_name = "cabanas/form.html"
    fields = ["nombre", "descripcion", "capacidad", "precio"]
    success_url = reverse_lazy("cabanas:list")

# Vista basada en clase: eliminación de una cabaña
class CabanaDeleteView(DeleteView):
    """ vista para eliminar una cabaña"""
    model = Cabana
    template_name = "cabanas/confirm_delete.html"
    success_url = reverse_lazy("cabanas:list")

# Ejemplo de vista basada en función
def start_cabanas(request):

    """Vista simple para mostrar página de inicio de cabañas."""
    cabanas = Cabana.objects.all()
    return render(request, "cabanas/inicio.html", {"cabanas": cabanas})
