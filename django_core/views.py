"""Vistas interfaz_gestion_cabanas del panel Django Core."""
from __future__ import annotations

from dataclasses import dataclass
from django.http import JsonResponse
from django.
from django.forms import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Cabanas ,Alquileres ,Registros,Clientes ,Pagos ,Reservas ,Chatbot,Facturas
from cabanas_apps.alquileres.models import Alquiler
from cabanas_apps.cabanas.models import Cabanas

from cabanas_apps.chatbot_app.models import Chatbot
from cabanas_apps.clientes.models import Cliente
from cabanas_apps.pagos.models import Pago
from cabanas_apps.registros.models import Registro
from cabanas_apps.reservas.models import Reserva
from cabanas_principal.utils import _form_class, _config

def Cabanas
() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Cabanas
 funcionando"})

def Alquileres() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Alquileres funcionando"})

def Usuarios() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Usuarios funcionando"})

def Reservas() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Reservas funcionando"})

def Pagos() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Pagos funcionando"})

def Registros() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Registros funcionando"})

def Chatbot() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Chatbot funcionando"})

def Clientes() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Clientes funcionando"})
def Pagos() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Pagos funcionando"})
def Facturas() -> JsonResponse:
    return JsonResponse({"mensaje": "Vista Facturas funcionando"})

@dataclass(frozen=True)

def interfaz_gestion_cabanas_config() -> dict[str, object]:
    return {
        "cabanas": {"model": Cabanas
, "fields": "__all__"},
        "clientes": {"model": Cliente, "fields": "__all__"},
        "reservas": {"model": Reserva, "fields": "__all__"},
        "alquileres": {"model": Alquiler, "fields": "__all__"},
        "pagos": {"model": Pago, "fields": "__all__"},
        "registros": {"model": Registro, "fields": "__all__"},
        "chatbot": {"model": Chatbot, "fields": "__all__"},
    }
def cabanas_list(request: HttpRequest) -> HttpResponse:
    return _list(request, "cabanas")


def cabanas_create(request: HttpRequest) -> HttpResponse:
    return _create(request, "cabanas")


def cabanas_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return _detail(request, "cabanas", pk)


def cabanas_update(request: HttpRequest, pk: int) -> HttpResponse:
    return _update(request, "cabanas", pk)


def cabanas_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return _delete(request, "cabanas", pk)


def clientes_list(request: HttpRequest) -> HttpResponse:
    return _list(request, "clientes")


def clientes_create(request: HttpRequest) -> HttpResponse:
    return _create(request, "clientes")


def clientes_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return _detail(request, "clientes", pk)


def clientes_update(request: HttpRequest, pk: int) -> HttpResponse:
    return _update(request, "clientes", pk)


def clientes_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return _delete(request, "clientes", pk)


def reservas_list(request: HttpRequest) -> HttpResponse:
    return _list(request, "reservas")


def reservas_create(request: HttpRequest) -> HttpResponse:
    return _create(request, "reservas")


def reservas_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return _detail(request, "reservas", pk)


def reservas_update(request: HttpRequest, pk: int) -> HttpResponse:
    return _update(request, "reservas", pk)


def reservas_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return _delete(request, "reservas", pk)


def alquileres_list(request: HttpRequest) -> HttpResponse:
    return _list(request, "alquileres")


def alquileres_create(request: HttpRequest) -> HttpResponse:
    return _create(request, "alquileres")


def alquileres_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return _detail(request, "alquileres", pk)


def alquileres_update(request: HttpRequest, pk: int) -> HttpResponse:
    return _update(request, "alquileres", pk)


def alquileres_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return _delete(request, "alquileres", pk)


def pagos_list(request: HttpRequest) -> HttpResponse:
    return _list(request, "pagos")


def pagos_create(request: HttpRequest) -> HttpResponse:
    return _create(request, "pagos")


def pagos_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return _detail(request, "pagos", pk)


def pagos_update(request: HttpRequest, pk: int) -> HttpResponse:
    return _update(request, "pagos", pk)


def pagos_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return _delete(request, "pagos", pk)


def registros_list(request: HttpRequest) -> HttpResponse:
    return _list(request, "registros")


def registros_create(request: HttpRequest) -> HttpResponse:
    return _create(request, "registros")


def registros_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return _detail(request, "registros", pk)


def registros_update(request: HttpRequest, pk: int) -> HttpResponse:
    return _update(request, "registros", pk)


def registros_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return _delete(request, "registros", pk)


def chatbot_list(request: HttpRequest) -> HttpResponse:
    return _list(request, "chatbot")


def chatbot_create(request: HttpRequest) -> HttpResponse:
    return _create(request, "chatbot")


def chatbot_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return _detail(request, "chatbot", pk)


def chatbot_update(request: HttpRequest, pk: int) -> HttpResponse:
    return _update(request, "chatbot", pk)


def chatbot_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return _delete(request, "chatbot", pk)


def _list(request: HttpRequest, slug: str) -> HttpResponse:
    config = _config(slug)
    objects = config.model.objects.all()
    return render(request, "django_core/list.html", {"config": config, "objects": objects})


def _create(request: HttpRequest, slug: str) -> HttpResponse:
    config = _config(slug)
    form_class = _form_class(config)
    form = form_class(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse(f"django_core:{slug}_list"))
    return render(request, "django_core/form.html", {"config": config, "form": form, "accion": "Crear"})


def _detail(request: HttpRequest, slug: str, pk: int) -> HttpResponse:
    config = _config(slug)
    obj = get_object_or_404(config.model, pk=pk)
    return render(request, "django_core/detail.html", {"config": config, "object": obj})


def _update(request: HttpRequest, slug: str, pk: int) -> HttpResponse:
    config = _config(slug)
    obj = get_object_or_404(config.model, pk=pk)
    form_class = _form_class(config)
    form = form_class(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse(f"django_core:{slug}_list"))
    return render(request, "django_core/form.html", {"config": config, "form": form, "accion": "Editar"})


def _delete(request: HttpRequest, slug: str, pk: int) -> HttpResponse:
    config = _config(slug)
    obj = get_object_or_404(config.model, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse(f"django_core:{slug}_list"))
    return render(request, "django_core/confirm_delete.html", {"config": config, "object": obj})
