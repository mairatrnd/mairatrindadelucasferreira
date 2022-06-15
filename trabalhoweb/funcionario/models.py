from django.db import models

class Funcionario(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    data_de_contratação = models.CharField(max_length=100)