from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.solicitarqr, name='solicitarqr'),
    path('<str:nuhsa>/', views.generarqr, name='generarqr')

]

