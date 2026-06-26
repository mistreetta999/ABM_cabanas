from django.urls import path
from . import views

app_name = "cabana_api"

urlpatterns = [
    path("", views.index, name="index"),
    path("cabanas/", views.lista_cabanas, name="lista_cabanas"),
]
