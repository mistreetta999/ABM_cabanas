"""URL configuration for cabanas_api project."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('reservas/', views.reservas, name='reservas'),
    path('alquileres/', views.alquileres, name='alquileres'),
    path('registros/', views.registros, name='registros'),
    path('', views.index, name='index')
]
