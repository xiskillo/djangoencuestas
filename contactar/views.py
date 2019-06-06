from django.shortcuts import render,redirect
from .forms import ContactarFormRegistro,ContactarFormInformacion
from django.urls import reverse
from django.core.mail import EmailMessage


def contactar_registro(request):
    contactar_registro=ContactarFormRegistro()
    
    if request.method == "POST":
                contactar_registro=ContactarFormRegistro(data=request.POST)
                
                if contactar_registro.is_valid:
                        nombre=request.POST.get('nombre', '')
                        apellidos=request.POST.get('apellidos', '')
                        nif=request.POST.get('nif', '')
                        email=request.POST.get('email', '')
                        user=request.POST.get('user', '')
                        pwd=request.POST.get('pwd', '')
                        pwd_confirmacion=request.POST.get('pwd_confirmacion', '')                        
                        mensaje=request.POST.get('mensaje', '')

                        
                       
                        email=EmailMessage("Mensaje Recibido solicitando Usuario y Contraseña para Encuestas","Nombre: {}\nApellidos: {}\nNIF: {}\nEMAIL: {}\nUsuario: {}\nContraseña: {}\nConfirmar Contraseña: {}\n\n\nMensaje: \n{}".format(nombre,apellidos,nif,email,user,pwd,pwd_confirmacion,mensaje),
                                "xiskillo@hotmail.com",["xiskillo@gmail.com"],reply_to=[email])

                        email.send()
                        return redirect(reverse('contactar_registro')+'?ok')
   
    
    return render(request, "contactar/contactar_registro.html",{'form': contactar_registro})


def contactar_informacion(request):
    contactar_informacion=ContactarFormInformacion()
    
    if request.method == "POST":
                contactar_informacion=ContactarFormInformacion(data=request.POST)
                
                if contactar_informacion.is_valid:
                        nombre=request.POST.get('nombre', '')                       
                        email=request.POST.get('email', '')
                        mensaje=request.POST.get('mensaje', '')
                        email=EmailMessage("Mensaje Recibido solicitando INFORMACIÓN","Nombre: {}\nEMAIL: {}\n\n\n\nMensaje: \n{}".format(nombre,email,mensaje),
                                "xiskillo@hotmail.com",["xiskillo@gmail.com"],reply_to=[email])

                        email.send()
                        return redirect(reverse('contactar_informacion')+'?ok')
   
    
    return render(request, "contactar/contactar_informacion.html",{'form': contactar_informacion})


    
