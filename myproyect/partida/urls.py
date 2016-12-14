from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^crear_partida/$', views.crear_partida, name='crear_partida'),
    url(r'^lista_de_partidas/$', views.lista_de_partidas, name='lista_de_partidas'),
    url(r'^partida/(?P<game>[0-9]+)/unirse_a_partida$', views.unirse_a_partida, name='unirse_a_partida'),
    url(r'^partida/(?P<game>[0-9]+)$', views.comenzar, name='comenzar'),
    url(r'^partida/(?P<game>[0-9]+)/borrar_partida/$', views.borrar_partida, name='borrar_partida'),
    url(r'^partida/(?P<game>[0-9]+)/turnoj1/$', views.turnoj1, name='turnoj1'),
    url(r'^partida/(?P<game>[0-9]+)/turnoj2/$', views.turnoj2, name='turnoj2'),
    url(r'^partida/(?P<game>[0-9]+)/turnoj3/$', views.turnoj3, name='turnoj3'),
    url(r'^partida/(?P<game>[0-9]+)/turnoj4/$', views.turnoj4, name='turnoj4'),
    url(r'^partida/(?P<game>[0-9]+)/turnoj5/$', views.turnoj5, name='turnoj5'),
]