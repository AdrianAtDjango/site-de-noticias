from django.db import models

class Paragrafos(models.Model):
    paragrafo = models.TextField() 

    def __str__(self):
        return self.paragrafo[:30]

class Noticia(models.Model):
    titulo = models.CharField()
    resumo = models.TextField(max_length=280)
    conteudo = models.ManyToManyField(Paragrafos)
    autor = models.CharField()
    tempo_leitura = models.IntegerField()
    data_criacao = models.DateField(auto_now=True)
    capa = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.titulo
