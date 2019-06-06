from rest_framework import viewsets
from .models import Paciente, AgendarExamen
from .serializer import PacienteSerializer,AgendarExamenSerializer

class PacienteViewSets (viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class AgendarExamenViewSets (viewsets.ModelViewSet):
    queryset = AgendarExamen.objects.all()
    serializer_class = AgendarExamenSerializer