from django.shortcuts import render, HttpResponse

# Create your views here.

def home_http(request):
    return HttpResponse("PAGINA HOME EN NUCLEO")


def home(request):
    return render(request,"nucleo/home.html")



