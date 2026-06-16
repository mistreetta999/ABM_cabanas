""'"module admin""""
from django.conf import settings
from django.contrib import admin
from models.cabana_models import Cabana
from models.clientes_models import Cliente
from models.reservas import Reserva
from models.alquileres import Alquiler
from models.registros import Registro

class AdminConfig:
    """Clase central para registrar todos los modelos en el panel de administración."""

    def registrar_cabana():
        class CabanaAdmin(admin.ModelAdmin):
            list_display = ("nombre", "capacidad", "precio_por_noche","precio_por_cabana")
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
AdminConfig.registrar_cabana()
AdminConfig.registrar_cliente()
AdminConfig.registrar_reserva()
AdminConfig.registrar_alquiler()
AdminConfig.registrar_registro()
