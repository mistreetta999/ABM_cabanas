from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path("lista/", views.lista_clientes, name="lista_clientes"),
]
