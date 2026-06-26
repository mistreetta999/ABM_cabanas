from django.urls import path
from . import views

app_name = "registros"

urlpatterns = [
    path("actividades/", views.lista_actividades, name="lista_actividades"),
]
