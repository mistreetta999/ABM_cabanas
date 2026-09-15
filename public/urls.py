"""URLs de la aplicación Public."""

from django.urls import path

from public.views import (
    AcercaDeTemplateView,
    AcercaDeView,
    ContactoTemplateView,
    ContactoView,
    HomeTemplateView,
    HomeView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("acerca-de/", AcercaDeView.as_view(), name="acerca_de"),
    path("contacto/", ContactoView.as_view(), name="contacto"),
    path("home-template/", HomeTemplateView.as_view(), name="home_template"),
    path(
        "acerca-de-template/", AcercaDeTemplateView.as_view(), name="acerca_de_template"
    ),
    path(
        "contacto-template/", ContactoTemplateView.as_view(), name="contacto_template"
    ),
]
