from django import forms



class NoticiasForm(forms.Form):

    titulo = forms.CharField(label="Titulo", widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el Título'}))
    mensaje = forms.CharField(label="Mensaje", widget = forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe el Mensaje', 'rows' : 6}))



class MensajeForm(forms.Form):

    titulo = forms.CharField(label="Titulo", widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el Título'}))
    mensaje = forms.CharField(label="Mensaje", widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el Mensaje'}))



