from django.shortcuts import render, HttpResponse, redirect, get_list_or_404, get_object_or_404
from push_notifications.models import APNSDevice, GCMDevice
from .forms import NoticiasForm, MensajeForm
from django.urls import reverse
import requests
import json
from encuestas.models import Pacientes
# from django.shortcuts import render_to_response
# from django.shortcuts import RequestContext

# Create your views here.





def notificaciones_push_individual(request):
    mensaje_form=MensajeForm()
    pacientes = get_list_or_404(Pacientes)


    if request.method == "POST":
                mensaje_form=MensajeForm(data=request.POST)
                
                if mensaje_form.is_valid:
                        titulo=request.POST.get('titulo', '')                       
                        mensaje=request.POST.get('mensaje', '')
                        id_android=request.POST.get('id_android', '')
                       

                        enviar_individual(titulo,mensaje,id_android)
                        return redirect(reverse('notificaciones_push_individual')+'?ok')
   
    
    return render(request, "notificaciones_push/notificaciones_push_individual.html",{'form': mensaje_form, 'pacientes':pacientes})




def notificaciones_push_noticias(request):
    noticias_form=NoticiasForm()
    
    if request.method == "POST":
                noticias_form=NoticiasForm(data=request.POST)
                
                if noticias_form.is_valid:
                        titulo=request.POST.get('titulo', '')                       
                        mensaje=request.POST.get('mensaje', '')
                       

                        enviar_noticias(titulo,mensaje)
                        return redirect(reverse('notificaciones_push_noticias')+'?ok')
   
    
    return render(request, "notificaciones_push/notificaciones_push_noticias.html",{'form': noticias_form})




def enviar_noticias(titulo, mensaje):

   
    url = 'https://onesignal.com/api/v1/notifications'
    payload = {
            "app_id": "0a094478-26f7-4064-8d31-1c4a23e16402",
            "included_segments": ["Active Users", "Inactive Users"],        
            "contents": { "en": mensaje, "es": mensaje},
            "headings": { "en": titulo, "es": titulo}
            }

    headers = {'content-type': 'application/json',
                'Authorization': 'Basic MWU2YTdkZmUtMmJhMy00YjAxLThhMjYtYzlkY2JhMjFjYTVm'}

    post = requests.post(url, data=json.dumps(payload), headers=headers)



def enviar_individual(titulo, mensaje, id_android):

   
    url = 'https://onesignal.com/api/v1/notifications'
    payload = {
            "app_id": "0a094478-26f7-4064-8d31-1c4a23e16402",
            "include_player_ids": [id_android],        
            "contents": { "en": mensaje, "es": mensaje},
            "headings": { "en": titulo, "es": titulo}
            }

    headers = {'content-type': 'application/json',
                'Authorization': 'Basic MWU2YTdkZmUtMmJhMy00YjAxLThhMjYtYzlkY2JhMjFjYTVm'}

    post = requests.post(url, data=json.dumps(payload), headers=headers)

    

def enviar_activos(request):

   
    url = 'https://onesignal.com/api/v1/notifications'
    payload = {
            "app_id": "0a094478-26f7-4064-8d31-1c4a23e16402",
            "included_segments": ["Active Users", "Inactive Users"],        
            "contents": { "en": "INGLEEE", "es": "Por favor, contesta las preguntas recibidas"},
            "headings": { "en": " TITULO INGLEEE", "es": "CONSULTA SI TIENES ENCUESTAS NUEVAS"}
            }

    headers = {'content-type': 'application/json',
                'Authorization': 'Basic MWU2YTdkZmUtMmJhMy00YjAxLThhMjYtYzlkY2JhMjFjYTVm'}

    post = requests.post(url, data=json.dumps(payload), headers=headers)

    return render(request, 'notificaciones_push/notificaciones_push.html')
    

def pushHttpResponse(request):
    return HttpResponse("PAGINA PUSH HTTRESPONSE")




def notificaciones_push(request):



    return render(request, 'notificaciones_push/notificaciones_push.html')

# def notificaciones_push(request):

#     message="RAY"

#     d = GCMDevice.objects.all()
#     d.send_message({"message": "Hi Android!"})

    

    

#     if request.method == "POST":
#         if 'code' in request.POST:
#             code = request.POST['code']

#             if code == 'android':
#                 print ('code == android')
#                 devices = GCMDevice.objects.all()
#                 devices.send_message({"message": "Hi Android!"})
#                 message = "message sent to android devices"

#             elif code == 'ios':
#                 print ('code == ios')
#                 devices = APNSDevice.objects.all()
#                 devices.send_message("Hi iOS!")
#                 message = "message sent to ios devices"
#             elif code == 'simple':
#                 print ('code == simple')
#                 device = APNSDevice.objects.get(registration_id='mi apns token')
#                 device.send_message(None, extra={"foo": "bar"})
#                 message = "simple message sent"

    
#     return render(request, 'notificaciones_push/notificaciones_push.html', {'message': message, 'd': d})



