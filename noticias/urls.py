from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_noticias, name='lista'),
    path('ler/<int:id>', views.ler_noticia, name='ler')
]