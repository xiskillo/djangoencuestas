from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from encuestas.models import Procedimientos, Pacientes
import base64

# Create your views here.

def qrHttpResponse(request):
    return HttpResponse("PAGINA QR EN APP QR")


def generarqr(request, nuhsa):
    n=nuhsa
    
    original = nuhsa
    originalbytes = original.encode("UTF-8")
    codificacion = base64.b64encode(originalbytes)
    
    return render(request,"qr/generarqr.html", {'n':n, 'c':codificacion})



def solicitarqr(request):
    pacientes = get_list_or_404(Pacientes)
    return render(request, 'qr/solicitarqr.html', {'pacientes':pacientes})
    