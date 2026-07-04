"""Formulario para crear o actualizar un cliente."""
from django import forms
from .models import Client

class ClienteForm(forms.ModelForm):
    """Formulario para crear o actualizar un cliente."""
    class Meta:
        """Meta class para ClienteForm."""
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono']
