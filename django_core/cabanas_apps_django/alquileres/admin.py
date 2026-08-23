""" archivo interfaz_gestion_cabanas"""
from django.contrib import admin as interfaz_gestion_cabanas
from .models import Alquiler

interfaz_gestion_cabanas.site.register(Alquiler)
