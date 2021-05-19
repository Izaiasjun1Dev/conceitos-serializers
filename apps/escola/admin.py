from django.contrib import admin
from .models import (
    Aluno, Curso, Matriculas
)


class AlunosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'surname',
        'rg',
        'cpf',
        'date_birth'
    )
    list_display_links = (
        'id', 'first_name')
    search_fields = (
        'first_name', 'cpf')
    list_per_page = 20

admin.site.register(Aluno, AlunosAdmin)

class CusrsosAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cod_curso',
        'level'
    )
    list_display_links = (
        'cod_curso', 'name')
    search_fields = (
        'name',
        'level'
    )
    
admin.site.register(Curso, CusrsosAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'aluno',
        'period'
    )
    list_display_links = ('id', 'aluno')

admin.site.register(Matriculas, MatriculaAdmin)