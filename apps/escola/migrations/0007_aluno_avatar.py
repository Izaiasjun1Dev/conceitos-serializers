# Generated by Django 3.2.4 on 2021-06-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0006_alter_aluno_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]