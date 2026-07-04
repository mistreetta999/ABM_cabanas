""" formulario para la aplicación de chatbot."""
from django import forms
from .models import Chatbot
class ChatbotForm(forms.ModelForm):
    """class para interactuar con el chatbot."""
    class Meta:
        """Meta información del formulario."""
        model = Chatbot
        fields = ['cliente', 'cabaña', 'fecha_inicio', 'fecha_fin']
