from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^lista_de_partidas/$', views.lista_de_partidas, name='lista_de_partidas'),
]