""" archivo para configurar el panel de administración de Django para los modelos de la aplicación de Cabanas. """
from typing import Any
from django.contrib import admin as interfaz_gestion_cabanas
from django.contrib.auth.mixins import AccessMixin
from django.views import View
from cabanas_apps.alquileres.models import Alquiler
from cabanas_apps.cabanas.models import Cabana
from cabanas_apps.clientes.models import Cliente
from cabanas_apps.registros.models import Registro
from cabanas_apps.reservas.models import Reserva

class AccesoConcedido(AccessMixin, View):
    """concede acceso a todos los usuarios sin restricciones."""

class AdminConfig:
    """Clase central para registrar todos los modelos en el panel de administración."""

    @staticmethod
    def registrar_cabana()->Any:
        """Registra la configuración del modelo Cabanas en el panel de administración."""
        class CabanaAdmin(interfaz_gestion_cabanas.ModelAdmin):
            """Configuración del panel de administración para Cabanas."""
            list_display = ("nombre", "capacidad", "precio_por_noche","precio_por_cabana")
            search_fields = ("nombre",)
        interfaz_gestion_cabanas.site.register(Cabana
, CabanaAdmin)

    @staticmethod
    def registrar_cliente()->Any:
        """Registra la configuración del modelo Cliente en el panel de administración."""
        class ClienteAdmin(interfaz_gestion_cabanas.ModelAdmin):
            """Configuración del panel de administración para Cliente."""
            list_display = ("nombre", "email", "telefono")
            search_fields = ("nombre", "email")
        interfaz_gestion_cabanas.site.register(Cliente, ClienteAdmin)

    @staticmethod
    def registrar_reserva()->Any:
        """Registra la configuración del modelo Reserva en el panel de administración."""
        class ReservaAdmin(interfaz_gestion_cabanas.ModelAdmin):
            """Configuración del panel de administración para Reservas."""
            list_display = ("Cabanas", "cliente", "fecha_inicio", "fecha_fin", "estado")
            list_filter = ("estado", "fecha_inicio", "fecha_fin")
        interfaz_gestion_cabanas.site.register(Reserva, ReservaAdmin)

    @staticmethod
    def registrar_alquiler()->Any:
        """Registra la configuración del modelo Alquiler en el panel de administración."""
        class AlquilerAdmin(interfaz_gestion_cabanas.ModelAdmin):
            list_display = ("Cabanas", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado")
            list_filter = ("pagado", "fecha_inicio", "fecha_fin")
        interfaz_gestion_cabanas.site.register(Alquiler, AlquilerAdmin)

    @staticmethod
    def registrar_registro()->Any:
        """Registra la configuración del modelo Registro en el panel de administración."""
        class RegistroAdmin(interfaz_gestion_cabanas.ModelAdmin):
            list_display = ("reserva", "cliente", "fecha_registro", "detalle")
            list_filter = ("fecha_registro",)
            search_fields = ("detalle",)
        interfaz_gestion_cabanas.site.register(Registro, RegistroAdmin)


# Ejecutar todos los registros al cargar el interfaz_gestion_cabanas
AdminConfig.registrar_cabana()
AdminConfig.registrar_cliente()
AdminConfig.registrar_reserva()
AdminConfig.registrar_alquiler()
AdminConfig.registrar_registro()
