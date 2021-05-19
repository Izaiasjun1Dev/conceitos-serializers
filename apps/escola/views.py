from django.db.models import fields
from django.views import generic
from rest_framework import serializers, viewsets, generics
from .models import (
    Aluno,
    Curso,
    Matriculas
)
from .serializers import (
    AlunoSerializer, CursoSerializer, ListaMatriculaSerializer, ListaMatriculadosCursoSerializer, MatriculaSerializer)

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """listagem de alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CusrosViewSet(viewsets.ModelViewSet):
    """listagem de cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    """listagem de Matriculas"""
    queryset = Matriculas.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatricula(generics.ListAPIView):
    """Listando as matriculas de um aluno"""

    def get_queryset(self):
        queryset = Matriculas.objects.filter(
            aluno_id=self.kwargs['pk']
        )
        return queryset

    serializer_class = ListaMatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """listando todos os alunos de um curso"""

    def get_queryset(self):
        queryset = Matriculas.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculadosCursoSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
