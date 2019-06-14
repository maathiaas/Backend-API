from rest_framework import viewsets
from .models import Paciente, AgendarExamen, TipoExamen, Espacialista, Examen
from .serializer import PacienteSerializer,AgendarExamenSerializer, TipoExamenSerializer, EspacialistaSerializer,ExamenSerializer

class PacienteViewSets (viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class AgendarExamenViewSets (viewsets.ModelViewSet):
    queryset = AgendarExamen.objects.all()
    serializer_class = AgendarExamenSerializer


class TipoExamenViewSets (viewsets.ModelViewSet):
    queryset = TipoExamen.objects.all()
    serializer_class = TipoExamenSerializer


class EspacialistaViewSets (viewsets.ModelViewSet):
    queryset = Espacialista.objects.all()
    serializer_class = EspacialistaSerializer


class ExamenViewSets (viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer