from rest_framework import serializers
# from .models import Songs



from django.contrib.auth.models import User
from encuestas.models import  Encuestas, Pacientes, Procedimientos
from encuestas.models import  Testing


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')
        
# Serializers define the API representation.
class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = ('id','nombre', 'apellidos','telefono', 'nuhsa','created', 'updated','id_android')

# Serializers define the API representation.
class ProcedimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimientos
        fields = ('id', 'nombre', 'descripcion', 'medico', 'created', 'updated')

class EncuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuestas
        fields = ('id', 'medico', 'paciente', 'procedimiento', 'pregunta', 'respuesta', 'created', 'updated')


class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = ('id', 'medico', 'paciente', 'procedimiento', 'pregunta', 'created', 'updated')
        
         



# class SongsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Songs
#         fields = ("title", "artist")






# class PreguntasSerializer(serializers.Serializer):    
#     facultativo=serializers.IntegerField()
#     pregunta=serializers.CharField(max_length=120)

#     # paciente = serializers.CharField(max_length=120)

#     def create(self, validated_data):
#         return Preguntas.objects.create(**validated_data)
    