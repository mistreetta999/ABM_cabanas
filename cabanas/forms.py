from django import forms
from .models import Cabanas

class CabanasForm(forms.ModelForm):
    """Formulario para la gestión de cabañas"""
    class Meta:
        """Metadatos del formulario"""
        model = Cabanas
        fields = ['nombre', 'descripcion', 'capacidad', 'precio']