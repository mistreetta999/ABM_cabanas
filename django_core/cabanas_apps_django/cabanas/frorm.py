from django import forms
from .models import Cabana   # Importa tu modelo correcto

class CabanaForm(forms.ModelForm):
    class Meta:
        model = Cabana       # Aquí debe ir tu clase Cabana
        fields = "__all__"
