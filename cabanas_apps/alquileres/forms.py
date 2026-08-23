from django import forms
from .models import Cabana

class CabanaForm(forms.ModelForm):
    class Meta:
        model = Cabana
        fields = ["nombre", "capacidad", "descripcion", "precio_por_noche", "disponible"]

        # Opcional: personalizar etiquetas y widgets
        labels = {
            "nombre": "Nombre de la cabaña",
            "capacidad": "Capacidad máxima",
            "descripcion": "Descripción",
            "precio_por_noche": "Precio por noche",
            "disponible": "Disponible",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio_por_noche": forms.NumberInput(attrs={"class": "form-control"}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
