"""
Module for shortcut functions to handle cabanas rendering and retrieval.
"""
from django.shortcuts import render, get_object_or_404
from .models import Cabanas

def render_with_cabanas(request, template_name, extra_context=None):
    """
    Atajo para renderizar cualquier template con todas las Cabanas cargadas.
    """
    cabanas = Cabanas.objects.all()
    context = {'cabanas': cabanas}
    if extra_context:
        context.update(extra_context)
    return render(request, template_name, context)

def get_cabana_or_404(pk):
    """
    Atajo para obtener una Cabana por su ID o lanzar 404 si no existe.
    """
    return get_object_or_404(Cabanas, pk=pk)
