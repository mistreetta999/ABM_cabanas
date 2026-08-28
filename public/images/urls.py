"""URLs de la aplicación Public."""

from django.urls import path
from . import views

app_name = "public"

urlpatterns = [
    # Páginas principales
    path("", views.HomeView.as_view(), name="home"),
    path("nosotros/", views.NosotrosView.as_view(), name="nosotros"),
    path("contacto/", views.ContactoView.as_view(), name="contacto"),

    # Catálogo de cabañas
    path("cabanas/", views.CabanaListView.as_view(), name="cabanas"),
    path("cabanas/<int:pk>/", views.CabanaDetailView.as_view(), name="cabana_detail"),

    # Disponibilidad y reservas públicas
    path("disponibilidad/", views.disponibilidad, name="disponibilidad"),
    path("reservar/<int:cabana_id>/", views.reservar_cabana, name="reservar_cabana"),
]
