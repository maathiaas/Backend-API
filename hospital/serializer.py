from rest_framework import serializers
from .models import Paciente, AgendarExamen, TipoExamen, Espacialista, Examen

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class AgendarExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendarExamen
        fields = '__all__'

class TipoExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoExamen
        fields = '__all__'


class EspacialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacialista
        fields = '__all__'

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = ('id','descripcion','paciente','tipo_examen','espacialista','pacienteName',
        'paciente_ape',
        'duracionExam',
        'precioExam')