from django.urls import path

from . import views


urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('cabanas/', views.PanelView.as_view(), name='panel_abm'),
    path('panel-django/', views.PanelView.as_view(), name='panel_django'),
    path('abm/', views.PanelView.as_view(), name='panel_abm_directo'),
    path('abm/clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('abm/clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('abm/clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('abm/clientes/<int:pk>/borrar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('abm/cabanas/', views.CabanaListView.as_view(), name='cabana_list'),
    path('abm/cabanas/nueva/', views.CabanaCreateView.as_view(), name='cabana_create'),
    path('abm/cabanas/<int:pk>/editar/', views.CabanaUpdateView.as_view(), name='cabana_update'),
    path('abm/cabanas/<int:pk>/borrar/', views.CabanaDeleteView.as_view(), name='cabana_delete'),
    path('abm/reservas/', views.ReservaListView.as_view(), name='reserva_list'),
    path('abm/reservas/nueva/', views.ReservaCreateView.as_view(), name='reserva_create'),
    path('abm/reservas/<int:pk>/editar/', views.ReservaUpdateView.as_view(), name='reserva_update'),
    path('abm/reservas/<int:pk>/borrar/', views.ReservaDeleteView.as_view(), name='reserva_delete'),
    path('abm/alquileres/', views.AlquilerListView.as_view(), name='alquiler_list'),
    path('abm/alquileres/nuevo/', views.AlquilerCreateView.as_view(), name='alquiler_create'),
    path('abm/alquileres/<int:pk>/editar/', views.AlquilerUpdateView.as_view(), name='alquiler_update'),
    path('abm/alquileres/<int:pk>/borrar/', views.AlquilerDeleteView.as_view(), name='alquiler_delete'),
    path('abm/pagos/', views.PagoListView.as_view(), name='pago_list'),
    path('abm/pagos/nuevo/', views.PagoCreateView.as_view(), name='pago_create'),
    path('abm/pagos/<int:pk>/editar/', views.PagoUpdateView.as_view(), name='pago_update'),
    path('abm/pagos/<int:pk>/borrar/', views.PagoDeleteView.as_view(), name='pago_delete'),
    path('abm/registros/', views.RegistroListView.as_view(), name='registro_list'),
    path('abm/registros/nuevo/', views.RegistroCreateView.as_view(), name='registro_create'),
    path('abm/registros/<int:pk>/editar/', views.RegistroUpdateView.as_view(), name='registro_update'),
    path('abm/registros/<int:pk>/borrar/', views.RegistroDeleteView.as_view(), name='registro_delete'),
]
