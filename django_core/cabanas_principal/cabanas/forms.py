from django import forms

class CabanaForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    capacidad = forms.IntegerField()
