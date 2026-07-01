"""Este archivo contiene las urls de la app reservas.
"""
from django.urls import path
from . import views
from . import reservas

APP_NAME = "reservas"

urlpatterns = [
    path("lista/", views.lista_reservas, name="lista_reservas"),
    
    
    path("", views.pagina_principal, name="pagina_principal"),
    path("reservas/", include("cabanas_apps.reservas.urls")),
]


