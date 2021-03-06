# Generated by Django 3.2.4 on 2021-06-02 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_auto_20210602_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='escola.contacts'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=20, verbose_name='Documento de cpf'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(max_length=10, verbose_name='Documento de rg'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='surname',
            field=models.CharField(max_length=15, verbose_name='Sobrenome nome'),
        ),
    ]
