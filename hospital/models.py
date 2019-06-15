
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

    def __str__(self):
        return self.rut_paciente

class AgendarExamen(models.Model):
    descripcion = models.CharField(max_length=300)
    hora = models.TimeField(null=True, blank=True)
    dia = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
       return self.usuario.rut_paciente



class TipoExamen(models.Model):
    Tipo1 = 'Examen tipo 1'
    Tipo2 = 'Examen tipo 2'
    Tipo3 = 'Examen tipo 3'
    Tipo4 = 'Examen tipo 4'
    Tipo5 = 'Examen tipo 5'
    Tipo6 = 'Examen tipo 6'
   
    ExamenTipo = [
        (Tipo1,'Examen tipo 1'),
        (Tipo2,'Examen tipo 2'),
        (Tipo3,'Examen tipo 3'),
        (Tipo4,'Examen tipo 4'),
        (Tipo5,'Examen tipo 5'),
        (Tipo6,'Examen tipo 6'),
        ]

    tipo_examen = models.CharField(max_length=2, choices=ExamenTipo)
    duracion = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=300)

    def __str__(self):
        return self.tipo_examen


class Espacialista(models.Model):
    F = 'Femenino'
    M = 'Masculino'
   
    Sexo = [(F,'Femenino'),(M,'Masculino')]

    rut_especialista = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    sexo = models.CharField(max_length=2, choices=Sexo)

    def __str__(self):
        return self.rut_especialista

class Examen(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_examen = models.ForeignKey(TipoExamen, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=300)
    espacialista = models.ForeignKey(Espacialista, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_examen

    def pacienteName(self):
        return self.paciente.nombres

    def paciente_ape(self):
        return (self.paciente.apellido_pat, self.paciente.apellido_mat)

    def duracionExam(self):
        return self.tipo_examen.duracion

    def precioExam(self):
        return self.tipo_examen.precio