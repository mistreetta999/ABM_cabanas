"""Rutas de la app alquileres."""
from django.urls import path

import django_core
from . import views

app_name = "alquileres"

urlpatterns = [
    path("django_core/", django_core.views("django_core.views.urls"), name="django_core_views"),
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("shortcuts/", django_core.views("django_core.views.urls"), name="shortcuts"),
    path("", views.alquileres_list, name="lista_alquileres"),
    path("reservas/", views.reservas_list, name="lista_reservas"),
    path("crear/", views.AlquilerCreateView.as_view(), name="crear_alquiler"),
    path("<int:pk>/editar/", views.AlquilerUpdateView.as_view(), name="editar_alquiler"),
    path("<int:pk>/eliminar/", views.AlquilerDeleteView.as_view(), name="eliminar_alquiler"),
]
