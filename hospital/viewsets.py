from rest_framework import viewsets
from .models import Paciente
from .serializer import PacienteSerializer

class PacienteViewSets (viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer