"""Formularios para la aplicación de alquileres."""
from django import forms
from .models import Alquiler

class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ["cliente", "cabana", "fecha_inicio", "fecha_fin", "monto"]

        labels = {
            "cliente": "Cliente",
            "cabana": "Cabaña",
            "fecha_inicio": "Fecha de inicio",
            "fecha_fin": "Fecha de fin",
            "monto": "Monto total",
        }

        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "cabana": forms.Select(attrs={"class": "form-control"}),
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "monto": forms.NumberInput(attrs={"class": "form-control"}),
        }
