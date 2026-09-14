"""Formulario para el modelo Registro."""
from django import forms
from .models import Registro


class RegistroForm(forms.ModelForm):
    """Formulario basado en el modelo Registro."""
    class Meta:
        """Configuración del formulario basado en el modelo Registro."""
        model = Registro
        fields = ["nombre", "descripcion", "fecha", "activo"]

        # Etiquetas más claras para el admin y los formularios
        labels = {
            "nombre": "Nombre del registro",
            "descripcion": "Descripción",
            "fecha": "Fecha de creación",
            "activo": "¿Está activo?",
        }

        # Widgets para que Django renderice el form con estilos básicos
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "fecha": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
