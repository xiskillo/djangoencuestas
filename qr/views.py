from django.shortcuts import render, HttpResponse

# Create your views here.

def qrHttpResponse(request):
    return HttpResponse("PAGINA QR EN APP QR")


def qrHtml(request):
    return render(request,"qr/qr.html")