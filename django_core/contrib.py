from django.contrib import admin
from cabanas_apps.models.cabana_models import Cabana
from cabanas_apps.models.clientes_models import Cliente
from cabanas_apps.models.reservas_models import Reserva
from cabanas_apps.models.alquileres_models import Alquiler
from cabanas_apps.models.registros_models import Registro

class ContribAdmin:
    """Clase central que organiza el registro de todos los modelos en el admin."""

    def registrar_cabana():
        class CabanaAdmin(admin.ModelAdmin):
            list_display = ("nombre", "capacidad", "precio_por_noche")
            search_fields = ("nombre",)
        admin.site.register(Cabana, CabanaAdmin)

    def registrar_cliente():
        class ClienteAdmin(admin.ModelAdmin):
            list_display = ("nombre", "email", "telefono")
            search_fields = ("nombre", "email")
        admin.site.register(Cliente, ClienteAdmin)

    def registrar_reserva():
        class ReservaAdmin(admin.ModelAdmin):
            list_display = ("cabana", "cliente", "fecha_inicio", "fecha_fin", "estado")
            list_filter = ("estado", "fecha_inicio", "fecha_fin")
        admin.site.register(Reserva, ReservaAdmin)

    def registrar_alquiler():
        class AlquilerAdmin(admin.ModelAdmin):
            list_display = ("cabana", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado")
            list_filter = ("pagado", "fecha_inicio", "fecha_fin")
        admin.site.register(Alquiler, AlquilerAdmin)

    def registrar_registro():
        class RegistroAdmin(admin.ModelAdmin):
            list_display = ("reserva", "cliente", "fecha_registro", "detalle")
            list_filter = ("fecha_registro",)
            search_fields = ("detalle",)
        admin.site.register(Registro, RegistroAdmin)


# Ejecutar todos los registros al cargar el admin
ContribAdmin.registrar_cabana()
ContribAdmin.registrar_cliente()
ContribAdmin.registrar_reserva()
ContribAdmin.registrar_alquiler()
ContribAdmin.registrar_registro()
