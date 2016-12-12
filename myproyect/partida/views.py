from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from partida.models import Partida, Mapa
from usuario.models import Usuario
from .forms import FormularioPartida


# Create your views here.


@login_required
def lista_de_partidas(request):

    partidas = Partida.objects.all()
    # asignamos a las partidas las cantidad actual de jugadores que estan esperando por jugarlas
    #Partida.objects.all().delete()
 
    return render(request, 'lista_de_partidas.html',
                  {'partidas': partidas})



@login_required
def crear_partida(request):
    if request.method == "POST":
        form = FormularioPartida(request.POST)
        if form.is_valid():
            partida = form.save(commit=False)
            partida.owner = request.user
            mapa = Mapa.objects.create()
            partida.mapa = mapa
            partida.save()
            #game_id = str(partida.id)
            return HttpResponseRedirect('/partida/' + str(partida.id))
    else:
        form = FormularioPartida()
        
    return render(request, 'crear_partida.html', {'form': form})

@login_required
def borrar_partida(request, game):
    partida = get_object_or_404(Partida, pk=game)
    partida.delete()
    return HttpResponseRedirect('/home')

@login_required
def unirse_a_partida(request, game):
    partida = get_object_or_404(Partida, pk=game)
    partida.jugador2 = request.user

    # actualiazmos la cantidad de jugadores que estan jugando la partida
    partida.cantjugadores += 1 
    partida.save()
    return render(request, 'comenzar_partida.html',
                  {'partida': partida})



@login_required
def comenzar(request, game):
    partida = get_object_or_404(Partida, pk=game)
    return render(request, 'comenzar_partida.html',
                  {'partida': partida})


@login_required
def turnoj1(request, game):
    partida = get_object_or_404(Partida, pk=game)
    mapa1 = partida.mapa
    mapa = get_object_or_404(Mapa, pk=mapa1.id)
    context = {
        "partida": partida,
        "mapa" : mapa,
    }
    return render(request, 'turnoj1.html', context)


@login_required
def turnoj2(request, game):
    partida = get_object_or_404(Partida, pk=game)
    context = {
        "partida": partida
    }
    return render(request, 'turnoj2.html', context)


@login_required
def turnoj3(request, game):
    partida = get_object_or_404(Partida, pk=game)
    context = {
        "partida": partida
    }
    return render(request, 'turnoj3.html', context)


@login_required
def turnoj4(request, game):
    partida = get_object_or_404(Partida, pk=game)
    context = {
        "partida": partida
    }
    return render(request, 'turnoj4.html', context)


@login_required
def turnoj5(request, game):
    partida = get_object_or_404(Partida, pk=game)
    context = {
        "partida": partida
    }
    return render(request, 'turnoj5.html', context)

