from django import forms
from .models import Alquiler

class AlquilerForm(forms.ModelForm):
    """Formulario para crear o actualizar un alquiler."""
    class Meta:
        """ Meta class for AlquilerForm."""
        model = Alquiler
        fields = ['cliente', 'cabaña', 'fecha_inicio', 'fecha_fin']
