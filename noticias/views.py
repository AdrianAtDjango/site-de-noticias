from django.shortcuts import render
from .models import Noticia, Paragrafos

def lista_noticias(request):
    noticias = Noticia.objects.all()

    context = {'noticias': noticias}
    return render(request, 'lista.html', context)

def ler_noticia(request, id):
    noticia = Noticia.objects.get(id=id)

    context = {'noticia': noticia}
    return render(request, 'ler.html', context)