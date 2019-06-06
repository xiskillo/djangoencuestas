from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404

from django.urls import reverse, reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Encuestas,Pacientes,Procedimientos
from .models import Testing

from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets

from encuestas.serializers import UserSerializer, PacientesSerializer, ProcedimientosSerializer, EncuestasSerializer 

from .forms import ProcedimientosForm,EncuestasForm,PacientesForm

from rest_framework.permissions import IsAuthenticated


# VISTAS PARA LA SECCCION DE ENCUESTAS Y PREGUNTAS

def encuestas(request):
    return HttpResponse("PAGINA ENCUESTAS EN APP ENCUESTAS")



def listar_encuestas(request):
    encuestas = get_list_or_404(Encuestas)
    return render(request, 'encuestas/listar_encuestas.html', {'encuestas':encuestas})


def detallar_encuestas(request, encuestas_id):
    encuestas = get_object_or_404(Encuestas, id=encuestas_id)
    return render(request, 'encuestas/detallar_encuestas.html', {'encuestas':encuestas})


class EncuestasCreate(CreateView):
    
    model=Encuestas
    # fields=['pregunta','respuesta','procedimiento','medico','paciente']
    form_class=EncuestasForm
    

    # def get_success_url(self):
    #     return reverse('listar_encuestas')
    success_url = reverse_lazy('listar_encuestas')


class EncuestasUpdate(UpdateView):
    
    model=Encuestas
    # fields=['pregunta','respuesta','procedimiento','medico','paciente']
    form_class=EncuestasForm
    template_name_suffix = '_update_form'
    

    # def get_success_url(self):
    #     return reverse('listar_encuestas')
    def get_success_url(self):
     return reverse_lazy('editar_encuestas', args=[self.object.id]) + '?ok'


class EncuestasDelete(DeleteView):

    model=Encuestas
    success_url = reverse_lazy('listar_encuestas')









#VISTAS PARA LA SECCION DE PACIENTES



def listar_pacientes(request):
    pacientes = get_list_or_404(Pacientes)
    return render(request, 'encuestas/listar_pacientes.html', {'pacientes':pacientes})


def detallar_pacientes(request, pacientes_id):
    pacientes = get_object_or_404(Pacientes, id=pacientes_id)
    return render(request, 'encuestas/detallar_pacientes.html', {'pacientes':pacientes})


class PacientesCreate(CreateView):
    
    model=Pacientes
    # fields=['nombre','apellidos','telefono','nuhsa']  
    form_class=PacientesForm 

    
    success_url = reverse_lazy('listar_pacientes')


class PacientesUpdate(UpdateView):
    
    model=Pacientes
    # fields=['nombre','apellidos','telefono','nuhsa']
    form_class=PacientesForm 
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
     return reverse_lazy('editar_pacientes', args=[self.object.id]) + '?ok'


class PacientesDelete(DeleteView):

    model=Pacientes
    success_url = reverse_lazy('listar_pacientes')










#VISTAS PARA LA SECCION DE PROCEDIMIENTOS



def listar_procedimientos(request):
    procedimientos = get_list_or_404(Procedimientos)
    return render(request, 'encuestas/listar_procedimientos.html', {'procedimientos':procedimientos})


def detallar_procedimientos(request, procedimientos_id):
    procedimientos = get_object_or_404(Procedimientos, id=procedimientos_id)
    return render(request, 'encuestas/detallar_procedimientos.html', {'procedimientos':procedimientos})


class ProcedimientosCreate(CreateView):
    
    model=Procedimientos
    form_class=ProcedimientosForm
    # fields=['nombre','descripcion','medico']   

    
    success_url = reverse_lazy('listar_procedimientos')


class ProcedimientosUpdate(UpdateView):
    
    model=Procedimientos
    form_class=ProcedimientosForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
     return reverse_lazy('editar_procedimientos', args=[self.object.id]) + '?ok'


class ProcedimientosDelete(DeleteView):

    model=Procedimientos
    success_url = reverse_lazy('listar_procedimientos')
    






# SECCION PARA TESTING SECCION PARA TESTING SECCION PARA TESTING SECCION PARA TESTING SECCION PARA TESTING

class TestingCreate(CreateView):
    
    model=Testing
    fields=['pregunta','procedimiento','medico','paciente']
    

    success_url = reverse_lazy('listar_encuestas')
    




# VISTAS PARA EL USO DE LA API REST


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PacientesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

    def get_queryset(self):
        """ PARAMETRIZAR SEGUN CONVENGA """
        queryset = Pacientes.objects.all()
        nuhsa = self.request.query_params.get('nuhsa', None)
        if nuhsa is not None:
            queryset = queryset.filter(nuhsa=nuhsa)
        
        return queryset

    
        



class ProcedimientosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Procedimientos.objects.all()
    serializer_class = ProcedimientosSerializer


class EncuestasViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    

    queryset = Encuestas.objects.all()
    serializer_class = EncuestasSerializer

    def get_queryset(self):
        """ PARAMETRIZAR SEGUN CONVENGA """
        queryset = Encuestas.objects.all()
        paciente = self.request.query_params.get('paciente', None)
        if paciente is not None:
            queryset = queryset.filter(paciente=paciente)
        
        return queryset



