from rest_framework import serializers
from .models import Paciente, AgendarExamen

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class AgendarExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendarExamen
        fields = '__all__'