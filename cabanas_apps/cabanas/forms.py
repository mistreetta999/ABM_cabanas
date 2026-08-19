"""Formulario para la aplicación de cabañas."""
from django import forms


class CabanasForm(forms.Form):
    """Formulario para capturar datos de una reserva."""
    cliente = forms.CharField(label="Cliente")
    cabana = forms.CharField(label="Cabaña")
    fecha_inicio = forms.DateField(label="Fecha de inicio")
    fecha_fin = forms.DateField(label="Fecha de fin")
