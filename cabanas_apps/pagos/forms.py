""" archivo de forms del proyecto django_local """
from django import forms
from .models import Pago
class PagosForm(forms.ModelForm):
    """class para crear o actualizar un pago."""
    class Meta:
        """Meta class para PagosForm."""
        model = Pago
        fields = ['cliente', 'cabaña', 'fecha_inicio', 'fecha_fin']
