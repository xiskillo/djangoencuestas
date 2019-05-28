from django import forms
from .models import Procedimientos

class ProcedimientosForm(forms.ModelForm):

    class Meta:
        model = Procedimientos
        fields = ['nombre', 'descripcion', 'medico']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            # 'medico' : forms.TextInput(attrs={'class':'form-control'})
        }