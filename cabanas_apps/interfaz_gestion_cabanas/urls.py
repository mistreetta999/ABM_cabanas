from django.urls import path
from . import views

app_name = "interfaz_gestion_cabanas"

urlpatterns = [
    path("", views.panel_gestion, name="panel_gestion"),
    path("lista/", views.lista_cabanas, name="lista_cabanas"),
]
