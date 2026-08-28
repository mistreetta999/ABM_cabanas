""" cabanas frormularioa"""
from django import forms
from .models import Cabana

class CabanaForm(forms.ModelForm):

    """ class cabana form"""
    class Meta:      
        """ class meta"""
        model = Cabana       # Aquí debe ir tu clase Cabana
        fields = "__all__"
