""" Formulario para la aplicación de cabañas."""
from django import forms
from .models import Reserva

class CabanasForm(forms.ModelForm):
    """Formulario para crear o actualizar una cabaña."""
    class Meta:
        """ Meta información del formulario."""
        model = Reserva
        fields = ['cliente', 'cabaña', 'fecha_inicio', 'fecha_fin']
