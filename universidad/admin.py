from django.contrib import admin
from .models import Programa, Curso, Estudiante


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "facultad", "anos_duracion")
    search_fields = ("nombre", "codigo", "facultad")
    list_filter = ("facultad",)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "nro_semestre", "programa")
    search_fields = ("nombre", "codigo")
    list_filter = ("programa", "nro_semestre")


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "id_estu", "correo", "programa", "f_ingreso")
    search_fields = ("nombre", "correo", "id_estu")
    list_filter = ("programa", "f_ingreso")
