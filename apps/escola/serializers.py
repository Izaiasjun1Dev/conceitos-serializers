from django.db import models
from rest_framework import serializers
from .models import (
    Aluno, Curso, Matriculas
)

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'id',
            'first_name',
            'surname',
            'rg',
            'cpf',
            'date_birth'
        ]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculas
        exclude = [] 

class ListaMatriculaSerializer(serializers.ModelSerializer):
    
    curso = serializers.ReadOnlyField(source='curso.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Matriculas
        fields = ['curso', 'period']

    def get_period(self, obj):
        return obj.get_period_display()

class ListaMatriculadosCursoSerializer(
    serializers.ModelSerializer):
    
    aluno_name = serializers.ReadOnlyField(source='aluno.first_name')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Matriculas
        fields = ['aluno_name', 'period']
        
    def get_period(self, obj):
        return obj.get_period_display()