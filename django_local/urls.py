"""URLs de la instancia django_local."""

from django.urls import path
from . import views

app_name = "django_local"

urlpatterns = [
    # Dashboard y resumen general
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("resumen/", views.resumen, name="resumen"),

    # CRUD de clientes
    path("clientes/", views.ClienteListView.as_view(), name="cliente_list"),
    path("clientes/<int:pk>/", views.ClienteDetailView.as_view(), name="cliente_detail"),
    path("clientes/nuevo/", views.ClienteCreateView.as_view(), name="cliente_create"),
    path("clientes/<int:pk>/editar/", views.ClienteUpdateView.as_view(), name="cliente_update"),
    path("clientes/<int:pk>/borrar/", views.ClienteDeleteView.as_view(), name="cliente_delete"),

    # CRUD de reservas
    path("reservas/", views.ReservaListView.as_view(), name="reserva_list"),
    path("reservas/<int:pk>/", views.ReservaDetailView.as_view(), name="reserva_detail"),
    path("reservas/nueva/", views.ReservaCreateView.as_view(), name="reserva_create"),
    path("reservas/<int:pk>/editar/", views.ReservaUpdateView.as_view(), name="reserva_update"),
    path("reservas/<int:pk>/borrar/", views.ReservaDeleteView.as_view(), name="reserva_delete"),

    # Facturas
    path("facturas/", views.FacturaListView.as_view(), name="factura_list"),
    path("facturas/<int:pk>/", views.FacturaDetailView.as_view(), name="factura_detail"),

    # Pagos
    path("pagos/", views.PagoListView.as_view(), name="pago_list"),
    path("pagos/<int:pk>/", views.PagoDetailView.as_view(), name="pago_detail"),

    # Auditoría y registros
    path("registros/", views.RegistroListView.as_view(), name="registro_list"),
]
