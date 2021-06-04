from uuid import uuid4
from rest_framework.test import APITestCase
from apps.escola.models import Curso
from django.urls import reverse


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            name='cusroteste1',
            cod_curso=str(uuid4()),
            description='descrptiontesgte1',
            level='B'
        )

    def falha(self):
        self.fail('ops!! falhou!')