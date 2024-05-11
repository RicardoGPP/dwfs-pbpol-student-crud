from django.db import models

class Aluno(models.Model):

    matricula = models.PositiveIntegerField(unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_ingresso = models.DateField()