from django.urls import path
from . import views
from .views import EncuestasCreate,EncuestasUpdate,EncuestasDelete
from .views import PacientesCreate,PacientesUpdate,PacientesDelete
from .views import ProcedimientosCreate,ProcedimientosUpdate,ProcedimientosDelete
from .views import TestingCreate




urlpatterns = [   

    # SECCION DE ENCUESTAS
    
    path('', views.listar_encuestas, name='listar_encuestas'),
    path('<int:encuestas_id>/', views.detallar_encuestas, name='detallar_encuestas'),
    path('crear_encuestas/', EncuestasCreate.as_view(), name='crear_encuestas'),
    path('editar_encuestas/<int:pk>/', EncuestasUpdate.as_view(), name='editar_encuestas'),
    path('borrar_encuestas/<int:pk>/', EncuestasDelete.as_view(), name='borrar_encuestas'),
    path('testing/', TestingCreate.as_view(), name='testing'),


    # SECCION DE PROCEDIMIENTOS

    path('procedimientos/', views.listar_procedimientos, name='listar_procedimientos'),
    path('procedimientos/<int:procedimientos_id>/', views.detallar_procedimientos, name='detallar_procedimientos'),
    path('procedimientos/crear_procedimientos/', ProcedimientosCreate.as_view(), name='crear_procedimientos'),
    path('editar_procedimientos/<int:pk>/', ProcedimientosUpdate.as_view(), name='editar_procedimientos'),
    path('borrar_procedimientos/<int:pk>/', ProcedimientosDelete.as_view(), name='borrar_procedimientos'),



    # SECCION DE PACIENTES



    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/<int:pacientes_id>/', views.detallar_pacientes, name='detallar_pacientes'),
    path('pacientes/crear_pacientes/', PacientesCreate.as_view(), name='crear_pacientes'),
    path('editar_pacientes/<int:pk>/', PacientesUpdate.as_view(), name='editar_pacientes'),
    path('borrar_pacientes/<int:pk>/', PacientesDelete.as_view(), name='borrar_pacientes')

]


