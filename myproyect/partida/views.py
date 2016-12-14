from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import JsonResponse
from partida.models import Partida
from usuario.models import Usuario
from django.contrib.auth.models import User
from .forms import FormularioPartida
from django.http import HttpResponseRedirect

# Create your views here.


@login_required
def lista_de_partidas(request):
    usuario = Usuario.objects.get(usuario=request.user.id)
    # si estaba jugando una partida ya no lo esta asi que lo desunimos de la partida que estaba unido
    usuario.partida = None
    usuario.turno = 0
    usuario.save()
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
    print("usuario.turno unirse_a_partida ANTEs")
    print(usuario.turno)
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
        return redirect('jugar_partida') 



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
def esperar_turno(request, pk):
    current_user = Usuario.objects.get(usuario=request.user.id)
    user = User.objects.get(usuario=current_user)
    turno = current_user.partida.turnos

    #if turno == current_user.turno:
     #   return redirect('jugar_partida', pasar=current_user.pk) 
    context = {
        'turno' : turno,
        'current_user' : current_user,
        'user' : user
    }
    print("EN ESPERAR TURNO")
    print("current_user turno")
    print(current_user.turno)
    print("partida turno")
    print(current_user.partida.turnos)
    return render(request,'esperar_turno.html', context) 
    

@login_required
def jugar_partida(request):
    current_user = Usuario.objects.get(usuario=request.user.id)
    partida = current_user.partida
    # devuelve los usuarios que estan jugando los partidas
    usuarios = Usuario.objects.filter(partida=partida)
    flag = 0
    print("current_user.turno")
    print(current_user.turno)
    print("TURNO ANTEs")
    print(partida.turnos    )
    if current_user.turno == partida.turnos:
        if request.method == 'POST':
            print("HICE POST")
            if partida.turnos < partida.cantidad_jugadores:
                partida.turnos = partida.turnos + 1
            else:
                partida.turnos = 1
            partida.save()
            flag = 1

    turno = partida.turnos
    print("TURNO DESPUES")
    print(turno)
    jugadores = User.objects.filter(usuario__partida=partida)
    context = {
        'jugadores' : jugadores,
        'current_user' : current_user,
        'turno' : turno
    }
    if flag == 1:
        return redirect('jugar_partida')
        
    return render(request,'jugar_partida.html', context) 

@login_required
def jugar_partida2(request):
    current_user = Usuario.objects.get(usuario=request.user.id)
    partida = current_user.partida
    # devuelve los usuarios que estan jugando los partidas
    usuarios = Usuario.objects.filter(partida=partida)
    # FLAG PASAR podria ser util sino me sale implementar de esta forma esta funcion
    pasar = 0
    print("current_user.turno")
    print(current_user.turno)
    print("TURNO ANTEs")
    print(partida.turnos)
    #if current_user.turno == partida.turnos + 1 or (current_user.turno == 1 and partida.turnos == 3):
    #if current_user.turno == partida.turnos:
    turno = partida.turnos
    print("TURNO DESPUES")
    print(turno)
    # si no se entra al anterior if, entonces se vuelve a renderizar
    # el template que habia llamado esta funcion
    # Todo lo anterior es para que un usuario no pueda saltear turnos actualizando la pag desde el browser
    # Esta consulta devuelve los user de auth asocioados a los usuarios que
    # estan jugando la partida, es para imprimir los nombres
    jugadores = User.objects.filter(usuario__partida=partida)
    context = {
        'jugadores' : jugadores,
        'current_user' : current_user,
        'turno' : turno
    }
    if current_user.turno == partida.turnos:
        return render(request,'jugar_partida.html', context)
    return render(request,'jugar_partida2.html',context)

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

