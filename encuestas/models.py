from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Pacientes(models.Model):

  nombre=models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombre del Paciente", default="Complete los campos..")
  apellidos=models.CharField(max_length=100, null=True, blank=True, verbose_name="Apellidos del Paciente")
  telefono=models.IntegerField(null=True, blank=True, verbose_name="Teléfono")
  nuhsa = models.CharField(max_length=20, unique=True, verbose_name="NUHSA" )
  created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")    
  updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
  id_android=models.CharField(max_length=100, null=True, blank=True, verbose_name="Identificado Android para Push")
  

  class Meta:

      verbose_name = "Paciente"
      verbose_name_plural = "Pacientes"
      ordering = ['-created']

  def __str__(self):
    return self.nombre+' '+self.apellidos


class Procedimientos(models.Model):

  nombre=models.CharField(max_length=50, verbose_name="Nombre del Procedimiento")
  descripcion=models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripción")
  medico=models.ForeignKey(User, verbose_name="Responsable Médico", null=True, blank=True, on_delete=models.CASCADE)  
  created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")    
  updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

  class Meta:

      verbose_name = "Procedimiento"
      verbose_name_plural = "Procedimientos"
      ordering = ['-created']
 

  def __str__(self):
    return self.nombre


class Encuestas(models.Model):
    
    medico=models.ForeignKey(User, verbose_name="Responsable Médico", null=True, blank=True, on_delete=models.CASCADE)
    paciente=models.ForeignKey(Pacientes, to_field='nuhsa', verbose_name="Paciente", null=True, blank=True, on_delete=models.CASCADE)
    procedimiento=models.ForeignKey(Procedimientos, verbose_name="Procedimiento Médico", null=True, blank=True, on_delete=models.CASCADE)
    pregunta=models.TextField(verbose_name="Pregunta de la Encuesta",null=True, blank=True)
    respuesta=models.TextField(verbose_name="Respuesta a la Pregunta",null=True, blank=True)
    
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")    
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:

      verbose_name = "Encuesta"
      verbose_name_plural = "Encuestas"
      ordering = ['-created']

    def __str__(self):
      return self.pregunta



class Testing(models.Model):
    
    medico=models.ForeignKey(User, verbose_name="Responsable Médico", null=True, blank=True, on_delete=models.CASCADE)
    paciente=models.ForeignKey(Pacientes, verbose_name="Paciente", null=True, blank=True, on_delete=models.CASCADE)
    procedimiento=models.ForeignKey(Procedimientos, verbose_name="Procedimiento Médico", null=True, blank=True, on_delete=models.CASCADE)
    pregunta=models.TextField(verbose_name="Pregunta de la Encuesta",null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")    
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    

    class Meta:

      verbose_name = "TESTING"
      verbose_name_plural = "TESTING"
      ordering = ['-created']

    def __str__(self):
      return self.pregunta


