from rest_framework.test import APITestCase
from apps.escola.models import Curso
from django.urls import reverse

class CursoTestCase(APITestCase):

    def setUp(self):
        self.list_urls = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            name='curso_teste', 
            description='descriptionsteste',
            level='B',
            cod_curso='codigoteste'
        )
        self.curso_2 = Curso.objects.create(
            name='curso_teste_2', 
            description='descriptionsteste_2',
            level='B',
            cod_curso='codigoteste_2'
        )
    
    def test_falador(self):
        self.fail('teste falha de proposito!')