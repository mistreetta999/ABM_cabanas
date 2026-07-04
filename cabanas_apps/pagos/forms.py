""" archivo de forms del proyecto django_local """
from django import forms
from .models import Pagos

class PagosForm(forms.ModelForm):
    """class para crear o actualizar un pago."""
    class Meta:
        """Meta class para PagosForm."""
        model = Pagos
        fields = ['cliente', 'cabaña', 'fecha_inicio', 'fecha_fin']
