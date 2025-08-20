from django.db import models


class Programa(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    facultad = models.CharField(max_length=100)
    anos_duracion = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100) 
    nro_semestre = models.PositiveIntegerField()
    programa = models.ForeignKey(
        Programa, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
        

class Estudiante(models.Model):
    id_estu = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    f_ingreso = models.DateField()
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes', blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.id_estu})"


# Create your models here.
