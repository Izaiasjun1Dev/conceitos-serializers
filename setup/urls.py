from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from apps.escola.views import (
    AlunosViewSet, CusrosViewSet, 
    ListaAlunosMatriculados, ListaMatricula, 
    MatriculaViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cusros', CusrosViewSet, basename='Cusos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatricula.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]
