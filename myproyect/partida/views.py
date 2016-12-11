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
    # si estaba jugando una partida ya no lo esta asi que lo desunimos de la partida que estaba unido
    usuario.partida = None
    partidas = Partida.objects.all()
    # asignamos a las partidas las cantidad actual de jugadores que estan esperando por jugarlas
    for partida in partidas:
        partida.jugando = Usuario.objects.filter(partida=partida).count()
        partida.save()
    #Partida.objects.all().delete()
 
    return render(request, 'lista_de_partidas.html',
                  {'partidas': partidas})

@login_required
def unirse_a_partida(request, pk):
    partida = Partida.objects.get(pk=pk)
    usuario = Usuario.objects.get(usuario=request.user.id)
    # unimos el usuario a la partida
    usuario.partida = partida
    usuario.save()
    # actualiazmos la cantidad de jugadores que estan jugando la partida
    partida.jugando = Usuario.objects.filter(partida=partida).count()
    partida.save()
    if partida.jugando != partida.cantidad_jugadores:
        return render(request,'unirse_a_partida.html', {partida : 'partida'})
    else:
        return redirect('jugar_partida', pk=partida.pk) 



@login_required
def abandonar_partida(request, pk):
    partida = Partida.objects.get(pk=pk)
    usuario = Usuario.objects.get(usuario=request.user.id)
    # unimos el usuario a la partida
    usuario.partida = None
    usuario.save()
    # actualiazmos la cantidad de jugadores que estan jugando la partida
    partida.jugando = Usuario.objects.filter(partida=partida).count()
    partida.save()
    return redirect('lista_de_partidas') 



@login_required
def jugar_partida(request, pk):
    partida = Partida.objects.get(pk=pk)
    jugadores = Usuario.objects.filter(partida=partida)

    return render(request,'jugar_partida.html', {jugadores : 'jugadores'}) 

@login_required
def crear_partida(request):
    if request.method == "POST":
        form = FormularioPartida(request.POST)
        if form.is_valid():
            partida = form.save(commit=False)
            usuario = Usuario.objects.get(usuario=request.user.id)
            partida.save()
            usuario.partida = partida
            usuario.save()
            #pk = partida.pk
            return redirect( 'unirse_a_partida',pk=partida.pk)
    else:
        form = FormularioPartida()
        
    return render(request, 'crear_partida.html', {'form': form})

