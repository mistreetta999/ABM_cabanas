from django.contrib import admin

from django_core.cabanas_apps_django.pagos.models import Pago


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "forma", "monto")
