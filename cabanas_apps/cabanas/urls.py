""" urls de cabanas"""
from django.urls import path
from . import views

app_name = "Cabana"

urlpatterns = [
    # Listado de cabañas
    path("", views.CabanaListView.as_view(), name="cabanas_list"),

    # Crear nueva cabaña
    path("crear/", views.CabanaCreateView.as_view(), name="crear_cabana"),

    # Detalle de una cabaña
    path("<int:pk>/", views.CabanaDetailView.as_view(), name="detalle_cabana"),

    # Editar cabaña
    path("<int:pk>/editar/", views.CabanaUpdateView.as_view(), name="editar_cabana"),

    # Eliminar cabaña
    path("<int:pk>/eliminar/", views.CabanaDeleteView.as_view(), name="eliminar_cabana"),
]
