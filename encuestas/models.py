from django.db import models

# Create your models here.


class Preguntas(models.Model):
    idpaciente=models.IntegerField()
    idfacultativo=models.IntegerField()
    pregunta=models.TextField()
    created=models.DateTimeField(auto_now_add=True)    
    updated=models.DateTimeField(auto_now=True)