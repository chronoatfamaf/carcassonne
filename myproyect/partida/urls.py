from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^lista_de_partidas/$', views.lista_de_partidas, name='lista_de_partidas'),
    url(r'^unirse_a_partida/(?P<pk>[0-9]+)/$', views.unirse_a_partida, name='unirse_a_partida'),
    url(r'^jugar_partida/$', views.jugar_partida, name='jugar_partida'),
    url(r'^jugar_partida2/$', views.jugar_partida2, name='jugar_partida2'),
    url(r'^esperar_turno/(?P<pk>[0-9]+)/$', views.esperar_turno, name='esperar_turno'),
    #url(r'^lista_de_partidas/unirse_a_partida/abandonar_partida/(?P<pk>[0-9]+)/$', views.abandonar_partida, name='abandonar_partida'),
    url(r'^crear_partida/$', views.crear_partida, name='crear_partida'),


]