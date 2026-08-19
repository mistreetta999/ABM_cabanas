""" urls"""
from django.http import HttpRequest, HttpResponse
from django.urls import path
from django.urls import path
from .views import (
    CabanaListView,
    CabanaDetailView,
    CabanaCreateView,
    CabanaUpdateView,
    CabanaDeleteView,
)

app_name = "cabanas_app

def lista_alquileres(_request: HttpRequest) -> HttpResponse:
    """ def lista"""
    return HttpResponse("Lista de alquileres")


def detalle_alquiler(_request, alquiler_id)->HttpResponse:
    """ def detalle"""
    return HttpResponse(f"Detalle del alquiler {alquiler_id}")


def crear_alquiler(_request: HttpRequest) -> HttpResponse:
    """ def crear"""
    return HttpResponse("Crear alquiler")


def actualizar_alquiler(_request, alquiler_id):
    """ def actualizar"""
    return HttpResponse(f"Actualizar alquiler {alquiler_id}")


def eliminar_alquiler(_request: HttpRequest, alquiler_id: int) -> HttpResponse:
    """def eliminar"""
    return HttpResponse(f"Eliminar alquiler {alquiler_id}")
"

urlpatterns = [
    path("", CabanaListView.as_view(), name="cabana_list"),
    path("<int:pk>/", CabanaDetailView.as_view(), name="cabana_detail"),
    path("crear/", CabanaCreateView.as_view(), name="cabana_create"),
    path("editar/<int:pk>/", CabanaUpdateView.as_view(), name="cabana_update"),
    path("eliminar/<int:pk>/", CabanaDeleteView.as_view(), name="cabana_delete"),
]
