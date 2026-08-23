from django.contrib import admin as interfaz_gestion_cabanas
from cabanas_apps.models.cabana_models import Cabanas

from cabanas_apps.models.clientes_models import Cliente
from cabanas_apps.models.reservas_models import Reserva
from cabanas_apps.models.alquileres_models import Alquiler
from cabanas_apps.models.registros_models import Registro

class ContribAdmin:
    """Clase central que organiza el registro de todos los modelos en el interfaz_gestion_cabanas."""

    def registrar_cabana():
        class CabanaAdmin(interfaz_gestion_cabanas.ModelAdmin):
            list_display = ("nombre", "capacidad", "precio_por_noche")
            search_fields = ("nombre",)
        interfaz_gestion_cabanas.site.register(Cabanas
, CabanaAdmin)

    def registrar_cliente():
        class ClienteAdmin(interfaz_gestion_cabanas.ModelAdmin):
            list_display = ("nombre", "email", "telefono")
            search_fields = ("nombre", "email")
        interfaz_gestion_cabanas.site.register(Cliente, ClienteAdmin)

    def registrar_reserva():
        class ReservaAdmin(interfaz_gestion_cabanas.ModelAdmin):
            list_display = ("Cabanas
", "cliente", "fecha_inicio", "fecha_fin", "estado")
            list_filter = ("estado", "fecha_inicio", "fecha_fin")
        interfaz_gestion_cabanas.site.register(Reserva, ReservaAdmin)

    def registrar_alquiler():
        class AlquilerAdmin(interfaz_gestion_cabanas.ModelAdmin):
            list_display = ("Cabanas
", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado")
            list_filter = ("pagado", "fecha_inicio", "fecha_fin")
        interfaz_gestion_cabanas.site.register(Alquiler, AlquilerAdmin)

    def registrar_registro():
        class RegistroAdmin(interfaz_gestion_cabanas.ModelAdmin):
            list_display = ("reserva", "cliente", "fecha_registro", "detalle")
            list_filter = ("fecha_registro",)
            search_fields = ("detalle",)
        interfaz_gestion_cabanas.site.register(Registro, RegistroAdmin)


# Ejecutar todos los registros al cargar el interfaz_gestion_cabanas
ContribAdmin.registrar_cabana()
ContribAdmin.registrar_cliente()
ContribAdmin.registrar_reserva()
ContribAdmin.registrar_alquiler()
ContribAdmin.registrar_registro()
