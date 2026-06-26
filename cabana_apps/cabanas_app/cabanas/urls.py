from django.urls import path
from . import views

app_name = "cabanas"

urlpatterns = [
    path("", views.index, name="index"),
    path("lista/", views.lista_cabanas, name="lista_cabanas"),
]
