from django import forms



class ContactarFormRegistro(forms.Form):
    nombre=forms.CharField(label="NOMBRE", required=True)
    apellidos=forms.CharField(label="APELLIDOS", required=True)
    nif=forms.CharField(label="NIF", required=True)
    email=forms.EmailField(label="EMAIL", required=True)
    user=forms.CharField(label="NOMBRE DE USUARIO DESEADO", required=True)
    pwd=forms.CharField(label="CONTRASEÑA DESEADA", required=True)    
    mensaje=forms.CharField(label="Observaciones", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje'}))


class ContactarFormInformacion(forms.Form):
    nombre=forms.CharField(label="NOMBRE", required=True)    
    email=forms.EmailField(label="EMAIL", required=True)   
    mensaje=forms.CharField(label="MENSAJE", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe tu mensaje'}))
 