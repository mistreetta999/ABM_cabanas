""" formularios de la app cabanas """
from django import forms
from django.db.models.base import Model


class CabanaForm(forms.ModelForm):
    """crear formulario de la app cabanas"""
    class Meta:
        """metadatos del formulario"""
        model = Model
        fields = '__all__'