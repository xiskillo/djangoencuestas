from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from graphos.renderers.morris import BarChart
from graphos.sources.model import SimpleDataSource
from graphos.sources.model import ModelDataSource
from encuestas.models import Encuestas,Pacientes,Procedimientos

from graphos.renderers.gchart import LineChart



def estadisticas_inicio(request):   



    return render(request, 'estadisticas/estadisticas_inicio.html')

def estadisticas_encuestas_procedimientos(request):
   

    
    queryset = get_list_or_404(Encuestas)
    data_source = ModelDataSource(queryset, fields=['contestacion','procedimiento_id','id'])
    
    chart = LineChart(data_source)
    context = {'grafico': chart}





    return render(request, 'estadisticas/estadisticas_encuestas_procedimientos.html', context)


def estadisticas_encuestas_nuhsa(request):
   

    
    queryset = get_list_or_404(Encuestas)
    data_source = ModelDataSource(queryset, fields=['paciente_id','procedimiento_id','id'])
    
    chart = LineChart(data_source)
    context = {'grafico': chart}





    return render(request, 'estadisticas/estadisticas_encuestas_nuhsa.html', context)



def estadisticas_procedimientos_medicos(request):
   

    
    queryset = get_list_or_404(Procedimientos)
    data_source = ModelDataSource(queryset, fields=['nombre','medico_id','id'])
    
    chart = LineChart(data_source)
    context = {'grafico': chart}





    return render(request, 'estadisticas/estadisticas_procedimientos_medicos.html', context)



