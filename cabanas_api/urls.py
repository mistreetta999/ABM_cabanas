"""URL configuration for cabanas_api project."""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pagos/', views.pagos, name='pagos'),
    path('clientes/', views.clientes, name='clientes'),
    path('registros/', views.registros, name='registros'),
    path('actividades/', views.actividades, name='actividades'),
    path('cabanas/', views.cabanas, name='cabanas'),
    path('reservas/', views.reservas, name='reservas'),
    path('alquileres/', views.alquileres, name='alquileres'),
    path('chatbot/', views.chatbot, name='chatbot'),    
    path('api/', views.api, name='api'),
    path('admin/', views.admin, name='admin'),
    path('Template/', views.Template, name='Template'),
]
