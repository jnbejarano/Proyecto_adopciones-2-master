from django import forms
from .models import Adopciones

class AdopcionesForm(forms.ModelForm):
    class Meta:
        model = Adopciones
        fields = "__all__"