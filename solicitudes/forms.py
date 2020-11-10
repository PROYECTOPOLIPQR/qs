from django import forms
from solicitudes.models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['name', 'email', 'phone','message']