from django import forms



class ContactarFormRegistro(forms.Form):
    nombre=forms.CharField(label="NOMBRE", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidos=forms.CharField(label="APELLIDOS", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    nif=forms.CharField(label="NIF", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="EMAIL", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    user=forms.CharField(label="NOMBRE DE USUARIO DESEADO", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd=forms.CharField(label="CONTRASEÑA",  required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))   
    pwd_confirmacion=forms.CharField(label="CONFIRMAR CONTRASEÑA",  required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))    
    mensaje=forms.CharField(label="Observaciones", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje'}))


class ContactarFormInformacion(forms.Form):
    nombre=forms.CharField(label="NOMBRE", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))    
    email=forms.EmailField(label="EMAIL", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))   
    mensaje=forms.CharField(label="MENSAJE", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje'}))
 