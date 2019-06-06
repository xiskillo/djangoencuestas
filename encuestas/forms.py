from django import forms
from .models import Procedimientos,Encuestas,Pacientes

class ProcedimientosForm(forms.ModelForm):

    class Meta:
        model = Procedimientos
        fields = ['nombre', 'descripcion', 'medico']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control'}),
            # 'medico' : forms.TextInput(attrs={'class':'form-control'})
        }




class EncuestasForm(forms.ModelForm):

    class Meta:
        model = Encuestas
        fields = ['pregunta', 'procedimiento', 'medico', 'paciente']
        widgets = {
            'pregunta' : forms.Textarea(attrs={'class':'form-control'}),
            
            
            
        }



class PacientesForm(forms.ModelForm):

    class Meta:
        model = Pacientes
        fields = ['nombre', 'apellidos', 'telefono', 'nuhsa']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),
            'nuhsa' : forms.TextInput(attrs={'class':'form-control'}),
            
            
        }
        

