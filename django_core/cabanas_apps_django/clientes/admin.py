""" admin"""
from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email")  # usa solo campos que existan
    search_fields = ("nombre", "email")

