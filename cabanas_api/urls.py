"""URL configuration for cabanas_api project."""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gestion/', views.gestion, name='gestion'),
    path('pagos/', views.pagos, name='pagos'),
    path('clientes/', views.clientes, name='clientes'),
]
