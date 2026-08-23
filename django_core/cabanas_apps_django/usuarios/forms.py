""" forms.py - Formulario de registro de usuario personalizado. """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from logging import getLogger

LOGGER = getLogger(__name__)

class RegistroForm(UserCreationForm):
    """Formulario de registro de usuario personalizado que utiliza el modelo Usuario."""
    class Meta:
        """Clase Meta para especificar las opciones del formulario."""
        model = Usuario
        fields = ["username", "email", "telefono", "direccion", "password1", "password2"]
