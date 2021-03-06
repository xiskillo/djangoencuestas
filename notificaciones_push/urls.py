from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.pushHttpResponse, name='pushHttpResponse'),
    path('notificaciones_push/', views.notificaciones_push, name='notificaciones_push'),    
    path('notificaciones_push/notificaciones_push_noticias/', views.notificaciones_push_noticias, name='notificaciones_push_noticias'),
    path('notificaciones_push/notificaciones_push_individual/', views.notificaciones_push_individual, name='notificaciones_push_individual'),
    path('notificaciones_push/notificaciones_push_avisos/', views.notificaciones_push_avisos, name='notificaciones_push_avisos'),
    

]

