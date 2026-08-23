from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_cabanas, name="lista_cabanas"),
    path("<int:cabana_id>/", views.detalle_cabana, name="detalle_cabana"),
]
