from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    nome = models.CharField(max_length=200)
    data = models.CharField(max_length=50)
    tarefa = models.TextField()

    def __str__(self):
        return self.titulo

class Conta(models.Model):
    nome_do_produto = models.CharField(max_length=100)
    data_do_pagamento = models.CharField(max_length=200)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_do_produto

class ContaApagar(models.Model):
    nome_do_produto = models.CharField(max_length=100)
    data_do_pagamento = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    status = models.CharField(max_length=50)


    def __str__(self):
        return self.nome_do_produto




     
