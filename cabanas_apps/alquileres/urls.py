""" urls"""
from django.http import HttpRequest, HttpResponse
from django.urls import path
from .views import (
    AlquilerListView,
    AlquilerCreateView,
    AlquilerUpdateView,
    AlquilerDeleteView,
    AlquilerDetailView,
)

app_name = "alquileres"

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


urlpatterns = [
    path("", AlquilerListView.as_view(), name="alquiler_list"),
    path("<int:pk>/", AlquilerDetailView.as_view(), name="alquiler_detail"),
    path("crear/", AlquilerCreateView.as_view(), name="alquiler_create"),
    path("editar/<int:pk>/", AlquilerUpdateView.as_view(), name="alquiler_update"),
    path("eliminar/<int:pk>/", AlquilerDeleteView.as_view(), name="alquiler_delete"),
]
