from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from partida.models import Partida
from usuario.models import Usuario
from .forms import FormularioPartida

# Create your views here.


@login_required
def lista_de_partidas(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    partidas = Partida.objects.all()
    # asignamos a las partidas las cantidad actual de jugadores que estan esperando por jugarlas
    for partida in partidas:
        partida.jugando = Usuario.filter(partida=partida).count()
        partida.save()
    #partida = Partida(cantidad_jugadores=5,jugando=2)
	#partidas = []
 	#   partidas.insert(0,partida)
    return render(request, 'lista_de_partidas.html',
                  {'partidas': partidas})
