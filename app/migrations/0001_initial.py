# Generated by Django 5.0.4 on 2024-05-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("matricula", models.PositiveIntegerField(unique=True)),
                ("data_nascimento", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=20)),
                ("data_ingresso", models.DateField()),
            ],
        ),
    ]
