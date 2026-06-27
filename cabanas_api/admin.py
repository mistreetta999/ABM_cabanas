from django.contrib import admin
from .models.cabana import Cabana
from .models.clientes import Cliente
from .models.reservas import Reserva
from .models.alquileres import Alquiler
from .models.registros import Registro

@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio_por_noche", "precio_por_cabana")
    search_fields = ("nombre",)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono")
    search_fields = ("nombre", "email")

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cabana", "cliente", "fecha_inicio", "fecha_fin", "estado")
    list_filter = ("estado", "fecha_inicio", "fecha_fin")

@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    list_display = ("cabana", "cliente", "fecha_inicio", "fecha_fin", "precio_total", "pagado")
    list_filter = ("pagado", "fecha_inicio", "fecha_fin")

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ("reserva", "cliente", "fecha_registro", "detalle")
    list_filter = ("fecha_registro",)
    search_fields = ("detalle",)
