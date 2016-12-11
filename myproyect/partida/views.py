from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from partida.models import Partida
from usuario.models import Usuario
from .forms import FormularioPartida


# Create your views here.


@login_required
def lista_de_partidas(request):
    partidas = Partida.objects.all()
    # asignamos a las partidas las cantidad actual de jugadores que estan esperando por jugarlas
    for partida in partidas:
        partida.jugando = Usuario.objects.filter(partida=partida).count()
        partida.save()

    return render(request, 'lista_de_partidas.html',
                  {'partidas': partidas})

@login_required
def crear_partida(request):
    if request.method == "POST":
        form = FormularioPartida(request.POST)
        if form.is_valid():
            partida = form.save(commit=False)
            partida.owner = request.user
            partida.save()
            #game_id = str(partida.id)
            return HttpResponseRedirect('/partida/' + str(partida.id))
    else:
        form = FormularioPartida()
        
    return render(request, 'crear_partida.html', {'form': form})

@login_required
def comenzar(request, game):
    partida = get_object_or_404(Partida, pk=game)
    return render(request, 'comenzar_partida.html',
                  {'partida': partida})


@login_required
def turnoj1(request, game):
    partida = get_object_or_404(Partida, pk=game)
    context = {
        "partida": partida
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

