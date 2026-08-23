"""Handles principales de django_core.core."""
from django.http import JsonResponse
from django.shortcuts import render


def handlers_core(request):
    """Devuelve el estado de los handles de core."""
    del request
    return JsonResponse({"core": "OK"})


def pagina_principal(request):
    """Muestra la pagina principal."""
    return render(request, "pagina_principal.html")


def listar_cabanas(request, cabanas_id=None):
    """Lista o identifica cabanas."""
    return JsonResponse({"cabanas_id": cabanas_id})


def listar_clientes(request, clientes_id=None):
    """Lista o identifica clientes."""
    return JsonResponse({"clientes_id": clientes_id})


def listar_reservas(request):
    """Lista reservas de ejemplo."""
    del request
    return JsonResponse({"reservas": []})


def detalle_reserva(request, reserva_id):
    """Detalle de reserva."""
    del request
    return JsonResponse({"reserva_id": reserva_id})


def crear_reserva(request, cliente_id, cabana_id):
    """Crea reserva de ejemplo."""
    del request
    return JsonResponse({"cliente_id": cliente_id, "cabana_id": cabana_id})


def borrar_reserva(request, reserva_id):
    """Borra reserva de ejemplo."""
    del request
    return JsonResponse({"reserva_id": reserva_id, "borrada": True})


def listar_alquileres(request):
    """Lista alquileres de ejemplo."""
    del request
    return JsonResponse({"alquileres": []})


def detalle_alquiler(request, reserva_id):
    """Detalle de alquiler."""
    del request
    return JsonResponse({"reserva_id": reserva_id})


def crear_alquiler(request, cliente_id, cabana_id):
    """Crea alquiler de ejemplo."""
    del request
    return JsonResponse({"cliente_id": cliente_id, "cabana_id": cabana_id})


def borrar_alquiler(request, reserva_id):
    """Borra alquiler de ejemplo."""
    del request
    return JsonResponse({"reserva_id": reserva_id, "borrado": True})


def listar_pagos(request):
    """Lista pagos de ejemplo."""
    del request
    return JsonResponse({"pagos": []})


def detalle_pago(request, reserva_id):
    """Detalle de pago."""
    del request
    return JsonResponse({"reserva_id": reserva_id})


def crear_pago(request, cliente_id, cabana_id):
    """Crea pago de ejemplo."""
    del request
    return JsonResponse({"cliente_id": cliente_id, "cabana_id": cabana_id})


def borrar_pago(request, reserva_id):
    """Borra pago de ejemplo."""
    del request
    return JsonResponse({"reserva_id": reserva_id, "borrado": True})
