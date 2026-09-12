"""URLs de la API de Cabañas."""

from django.urls import path
from cabanas_api.views import ApiHomeView
from cabanas_api.views import  AlquilerListView
from cabanas_api.views import  AlquilerDetailView
from cabanas_api.views import  FacturaListView
from cabanas_api.views import   ClienteListView
from cabanas_api.views import   PagoListView
from cabanas_api.views import   RegistroListView
from cabanas_api.views import   CabanaListView

urlpatterns = [
    path("", ApiHomeView.as_view(), name="api_home"),

    # Endpoints de alquileres
    path("alquileres/", AlquilerListView.as_view(), name="alquiler_list"),
    path("alquileres/<int:pk>/", AlquilerDetailView.as_view(), name="alquiler_detail"),

    # Endpoints de clientes
    path("clientes/", ClienteListView.as_view(), name="cliente_list"),

    # Endpoints de pagos
    path("pagos/", PagoListView.as_view(), name="pago_list"),

    # Endpoints de registros
    path("registros/", RegistroListView.as_view(), name="registro_list"),

    # Endpoints de cabañas
    path("cabanas/", CabanaListView.as_view(), name="cabana_list"),

    # Endpoints de facturas
    path("facturas/", FacturaListView.as_view(), name="factura_list"),
]
