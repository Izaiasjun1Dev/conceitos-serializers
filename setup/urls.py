from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from apps.escola.views import (
    AlunosViewSet, AlunosViewSets, CusrosViewSet,
    ListaAlunosMatriculados, ListaMatricula,
    MatriculaViewSet)
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CusrosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatricula.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
    path('alunov2/', AlunosViewSets.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
