""" archivo interfaz_gestion_cabanas.py para registrar los modelos en el panel de administración de Django """
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Reserva, Alquiler, Pago, Factura, ActividadCabana
# Registrar cada modelo en el panel de administración
interfaz_gestion_cabanas.site.register(Reserva)
interfaz_gestion_cabanas.site.register(Alquiler)
interfaz_gestion_cabanas.site.register(Pago)
interfaz_gestion_cabanas.site.register(Factura)
interfaz_gestion_cabanas.site.register(ActividadCabana)
