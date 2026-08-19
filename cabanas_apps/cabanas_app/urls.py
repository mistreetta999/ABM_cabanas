""" gestion cabanas urls"""
from django.urls import path
from .views import (
    crear_cabana,
    detalle_cabana,
    editar_cabana,
    eliminar_cabana,
)
apps_name = ["gestion_cabanas"]

urlpatterns = [
    path('<int:cabana_id>/', detalle_cabana, name='detalle_cabana'),
    path('crear/', crear_cabana, name='crear_cabana'),
    path('editar/<int:cabana_id>/', editar_cabana, name='editar_cabana'),
    path('eliminar/<int:cabana_id>/', eliminar_cabana, name='eliminar_cabana'),
]
