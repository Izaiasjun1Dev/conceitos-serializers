# Generated by Django 3.2.4 on 2021-06-02 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_auto_20210602_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='contacts',
        ),
        migrations.AddField(
            model_name='aluno',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alunos_contatos', to='escola.contacts'),
        ),
    ]
