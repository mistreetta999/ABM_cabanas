"""urls.py de la app clientes"""
from django.urls import path

import django_core
from . import views

app_name = "clientes"

urlpatterns = [
    path("django_core/", django_core.views("django_core.views.urls"), name="django_core_views"),
    path("shortcut/", django_core.views("django_core.views.urls"), name="shortcut"),
    path("shortcuts/", django_core.views("django_core.views.urls"), name="shortcuts"),
    path("interfaz_gestion_cabanas/", views.lista_clientes, name="lista_clientes"),
    path("", views.lista_clientes, name="lista_clientes"),
    path("home/", views.ClientesHomeView.as_view(), name="home"),
    path(
        "clientes/<int:pk>/",
        views.ClienteDetailView.as_view(),
        name="detalle_cliente",
    ),
    path(
        "clientes/<int:pk>/editar/",
        views.ClienteUpdateView.as_view(),
        name="editar_cliente",
    ),
    path(
        "clientes/<int:pk>/eliminar/",
        views.ClienteDeleteView.as_view(),
        name="eliminar_cliente",
    ),
]
