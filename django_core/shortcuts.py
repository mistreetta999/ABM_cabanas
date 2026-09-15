"""
Atajos y utilidades para renderizar templates y obtener objetos de cabanas_api.
"""

from django.shortcuts import get_object_or_404, render

from cabanas_api.models import Alquiler, Cabana, Cliente, Pago, Reserva


def object_or_404(model, pk):
    """
    Obtiene un objeto de cualquier modelo por su ID o lanza 404 si no existe.
    """
    return get_object_or_404(model, pk=pk)


def render_with_cabanas(request, template_name, extra_context=None):
    """
    Renderiza cualquier template con todas las cabañas cargadas.
    """
    cabanas = getattr(Cabana, "objects").all()
    context = {"cabanas": cabanas}
    if extra_context:
        context.update(extra_context)
    return render(request, template_name, context)


def get_cabana_or_404(pk):
    """
    Obtiene una cabaña por su ID o lanza 404 si no existe.
    """
    return get_object_or_404(Cabana, pk=pk)


def get_cliente_or_404(pk):
    """
    Obtiene un cliente por su ID o lanza 404 si no existe.
    """
    return get_object_or_404(Cliente, pk=pk)


def get_reserva_or_404(pk):
    """
    Obtiene una reserva por su ID o lanza 404 si no existe.
    """
    return get_object_or_404(Reserva, pk=pk)


def get_alquiler_or_404(pk):
    """
    Obtiene un alquiler por su ID o lanza 404 si no existe.
    """
    return get_object_or_404(Alquiler, pk=pk)


def get_pago_or_404(pk):
    """
    Obtiene un pago por su ID o lanza 404 si no existe.
    """
    return get_object_or_404(Pago, pk=pk)
