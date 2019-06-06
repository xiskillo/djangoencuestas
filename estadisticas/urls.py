from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.estadisticas_inicio, name='estadisticas'),
    path('encuestas_procedimientos/', views.estadisticas_encuestas_procedimientos, name='estadisticas_encuestas_procedimientos'),
    path('encuestas_nuhsa/', views.estadisticas_encuestas_nuhsa, name='estadisticas_encuestas_nuhsa'),
    path('procedimientos_medicos/', views.estadisticas_procedimientos_medicos, name='estadisticas_procedimientos_medicos'),
    

]