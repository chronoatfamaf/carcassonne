from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from partida.models import Partida
from usuario.models import Usuario
from django.contrib.auth.models import User
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
    # asignamos el turno del actual jugador como la cantidad de jugadores jugando (esperando jugar) mas 1
    # ya que si estamos en esta funcion se cumple partida.jugando < partida.cantidad_jugadores
    # y el turno se asgina por orden de llegada, es decir, el que se unio ultimo a la partida juega ultimo
    # y asi
    #sino tiene asignado turno se lo asignamos
    if usuario.turno == 0:
        usuario.turno = partida.jugando + 1

    # unimos el usuario a la partida
    print("usuario.turno en unirse_a_partida")
    print(usuario.turno)
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
    # desunimos el usuario a la partida
    usuario.partida = None
    # reseteamos el turno del usuario
    usuario.turno = 0
    usuario.save()
    # actualiazmos la cantidad de jugadores que estan jugando la partida
    partida.jugando = Usuario.objects.filter(partida=partida).count()
    partida.save()
    return redirect('lista_de_partidas') 

@login_required
def jugar_partida(request, pk):
    current_user = Usuario.objects.get(usuario=request.user.id)
    partida = Partida.objects.get(pk=pk)
    # devuelve los usuarios que estan jugando los partidas
    usuarios = Usuario.objects.filter(partida=partida)
    # asignamos el turno siguiente de la partida
    # es decir, le toca jugar al usuario cuyo usuario.turno == turno
    turno = partida.turnos
    # si el turno de current_user es el turno de la partida YA jugado + 1
    # entonces le toca jugar a current_user
    # si el turno de la partida es el ultimo entonces le toca al primer jugador (usuario.turno = 1)
    # por lo que se actualiza el turno de la partida (partida.turnos++)
    if (current_user.turno == turno+1 or (current_user.turno == 1 and turno == partida.cantidad_jugadores)):
        if turno == partida.cantidad_jugadores:
            turno = 1
        else:
            turno = turno + 1
        partida.turnos = turno
        partida.save()
    # si no se entra al anterior if, entonces se vuelve a renderizar
    # el template que habia llamado esta funcion
    # Todo lo anterior es para que un usuario no pueda saltear turnos actualizando la pag desde el browser
    # Esta consulta devuelve los user de auth asocioados a los usuarios que
    # estan jugando la partida, es para imprimir los nombres
    jugadores = User.objects.filter(usuario__partida=partida)
    print("JUGADORES")
    print(jugadores)
    print("TURNO")
    print(turno)
    print("current_user.turno")
    print(current_user.turno)
    context = {
        'jugadores' : jugadores,
        'current_user' : current_user,
        'turno' : turno
    }
    
    return render(request,'jugar_partida.html', context) 



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

