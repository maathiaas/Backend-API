
from django.db import models

# Create your models here.

class Paciente(models.Model):
    rut_paciente = models.CharField(max_length=9, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido_pat = models.CharField(max_length=100)
    apellido_mat = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    ocupacion = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    prevision = models.CharField(max_length=200)


class AgendarExamen(models.Model):
    descripcion = models.CharField(max_length=300)
    hora = models.TimeField(null=True, blank=True)
    dia = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(Paciente, on_delete=models.CASCADE)