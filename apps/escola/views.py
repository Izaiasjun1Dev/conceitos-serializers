from rest_framework import (
    status,
    viewsets,
    generics
)
from .models import (
    Aluno,
    Curso,
    Matriculas
)
from rest_framework.response import Response
from .serializers import (
    AlunoSerializer,
    AlunoSerializerV2,
    CursoSerializer,
    ListaMatriculaSerializer,
    ListaMatriculadosCursoSerializer,
    MatriculaSerializer)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class AlunosViewSet(viewsets.ModelViewSet):
    """listagem de alunos e alunas"""
    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class CusrosViewSet(viewsets.ModelViewSet):
    """listagem de cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # salva os dados dispostos se forem
            # validos conforme o passo anterios
            serializer.save()

            # Cria um response contendo os dados
            # salvos e retorna um status code 200
            response = Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
            # Captura o id que está sendo criado
            # E o converte em string
            id = str(serializer.data['id'])
            # Cria o Location para auto documentação da api
            response['Location'] = request.build_absolute_uri() + id

            return response


class MatriculaViewSet(viewsets.ModelViewSet):
    """listagem de Matriculas"""
    queryset = Matriculas.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'put', 'post', 'path']

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(MatriculaViewSet, self).dispatch(*args, **kwargs)


class ListaMatricula(generics.ListAPIView):
    """Listando as matriculas de um aluno"""

    def get_queryset(self):
        queryset = Matriculas.objects.filter(
            aluno_id=self.kwargs['pk']
        )
        return queryset

    serializer_class = ListaMatriculaSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """listando todos os alunos de um curso"""

    def get_queryset(self):
        queryset = Matriculas.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculadosCursoSerializer


class AlunosViewSets(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializerV2
