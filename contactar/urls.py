from django.urls import path
from . import views




urlpatterns=[

    path('registro/', views.contactar_registro, name="contactar_registro"),
    path('', views.contactar_informacion, name="contactar_informacion"),
    
]
