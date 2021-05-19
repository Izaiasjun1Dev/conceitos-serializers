import uuid
from django.db import models

class Aluno(models.Model):
    first_name = models.CharField(
        'primeiro nome', 
        max_length=15
        )
    surname = models.CharField(
        'sobrenome nome', max_length=15)
    rg = models.CharField(
        'documento de rg', max_length=10)
    cpf = models.CharField(
        'documento de cpf', max_length=20)
    date_birth = models.DateField()

    def __str__(self):
        return self.first_name

class Curso(models.Model):
    Nivel = (
        ('B', 'Básico'),
        ('I', 'Intermediario'),
        ('A', 'Avançado')
    )
    name = models.CharField(
        'Nome do curso', max_length=30)
    cod_curso = models.UUIDField(
        default=uuid.uuid4, 
        editable=False
    )
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1, 
        default='B',
        choices=Nivel, 
        null=False,
        blank=False
    )
    def __str__(self):
            return f'Name: {self.description}, Description: {self.description}'

class Matriculas(models.Model):
    Period = (
        ('M', 'Manha'),
        ('T', 'Tarde'),
        ('N', 'Noite')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    period = models.CharField(
        'Periodo',
        max_length=1, 
        choices=Period, 
        blank=False, 
        null=False, 
        default='M'
    )