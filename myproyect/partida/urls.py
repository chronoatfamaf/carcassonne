from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^lista_de_partidas/$', views.lista_de_partidas, name='lista_de_partidas'),
    url(r'^lista_de_partidas/unirse_a_partida/(?P<pk>[0-9]+)/$', views.unirse_a_partida, name='unirse_a_partida'),
    url(r'^lista_de_partidas/unirse_a_partida/jugar_partida/(?P<pasar>[0-9]+)/$', views.jugar_partida, name='jugar_partida'),
    #url(r'^lista_de_partidas/unirse_a_partida/abandonar_partida/(?P<pk>[0-9]+)/$', views.abandonar_partida, name='abandonar_partida'),
    url(r'^lista_de_partidas/crear_partida/$', views.crear_partida, name='crear_partida'),


]