"""Este archivo contiene las urls de la app cabanas.
"""
from django.urls import path

from cabanas_apps.models import Pago
from . import views
from .views import alquileres
from .views import Pagos




urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('cabanas/', views.PanelView.as_view(), name='panel_cabanas_api'),
    path('panel-django/', views.PanelView.as_view(), name='panel_django'),
    path('cabanas_api/', views.PanelView.as_view(), name='panel_cabanas_api_directo'),
    path('cabanas_api/clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('cabanas_api/clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('cabanas_api/clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('cabanas_api/clientes/<int:pk>/borrar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('cabanas_api/cabanas/', views.CabanaListView.as_view(), name='cabana_list'),
    path('cabanas_api/cabanas/nueva/', views.CabanaCreateView.as_view(), name='cabana_create'),
    path('cabanas_api/cabanas/<int:pk>/editar/', views.CabanaUpdateView.as_view(), name='cabana_update'),
    path('cabanas_api/cabanas/<int:pk>/borrar/', views.CabanaDeleteView.as_view(), name='cabana_delete'),
    path('cabanas_api/reservas/', views.ReservaListView.as_view(), name='reserva_list'),
    path('cabanas_api/reservas/nueva/', views.ReservaCreateView.as_view(), name='reserva_create'),
    path('cabanas_api/reservas/<int:pk>/editar/', views.ReservaUpdateView.as_view(), name='reserva_update'),
    path('cabanas_api/reservas/<int:pk>/borrar/', views.ReservaDeleteView.as_view(), name='reserva_delete'),
    path('cabanas_api/alquileres/', views.AlquilerListView.as_view(), name='alquiler_list'),
    path('cabanas_api/alquileres/nuevo/', views.AlquilerCreateView.as_view(), name='alquiler_create'),
    path('cabanas_api/alquileres/<int:pk>/editar/', views.AlquilerUpdateView.as_view(), name='alquiler_update'),
    path('cabanas_api/alquileres/<int:pk>/borrar/', views.AlquilerDeleteView.as_view(), name='alquiler_delete'),
    path('cabanas_api/pagos/', views.PagoListView.as_view(), name='pago_list'),
    path('cabanas_api/pagos/nuevo/', views.PagoCreateView.as_view(), name='pago_create'),
    path('cabanas_api/pagos/<int:pk>/editar/', views.PagoUpdateView.as_view(), name='pago_update'),
    path('cabanas_api/pagos/<int:pk>/borrar/', views.PagoDeleteView.as_view(), name='pago_delete'),
    path('cabanas_api/registros/', views.RegistroListView.as_view(), name='registro_list'),
    path('cabanas_api/registros/nuevo/', views.RegistroCreateView.as_view(), name='registro_create'),
    path('cabanas_api/registros/<int:pk>/editar/', views.RegistroUpdateView.as_view(), name='registro_update'),
    path('cabanas_api/registros/<int:pk>/borrar/', views.RegistroDeleteView.as_view(), name='registro_delete'),
]
