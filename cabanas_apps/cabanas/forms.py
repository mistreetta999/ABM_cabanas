"""Formulario para la aplicación de cabañas."""
from django import forms
from .models import Cabana   # Importa tu modelo, no la clase base

class CabanaForm(forms.ModelForm):
    """ class form"""
    class Meta:
        """ class meta"""
        model = Cabana       # Aquí debe ir tu modelo Cabana
        fields = "__all__"   # O lista explícita de campos
