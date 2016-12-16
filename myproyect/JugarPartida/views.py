from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import os
from django.utils import timezone
from django.contrib.auth import authenticate, login
from PIL import Image
from .models import Partida, Jugador, Pieza

def crearpartida(request):
  template = loader.get_template('JugarPartida/CrearPartida.html')
  context = {}
  return HttpResponse(template.render(context, request))

def partidacreada(request):
  nombreJugadores = ['Mateo', 'Juan', 'Pedro', 'Marcos', 'Esteban']
  cantJug = int(request.POST['numeromaximodejugadores'][0])
  for x in xrange(0, cantJug):
    J = Jugador(nombre=nombreJugadores[x])
    J.save()
  for y in xrange(1, 72):
    if y < 10:
      Pieza(esDescartada=False, imagenAsociada ='0' + str(y) + '.png' )
    else :
      Pieza(esDescartada=False, imagenAsociada = str(y) + '.png' )
    
  P = Partida(nombre = request.POST['nombre'],
                fechaInicio = str(timezone.now()), esFinalizado = 'N', piezaEnJuego=1)
  P.save()
  template = loader.get_template('JugarPartida/PartidaCreada.html')

  context = {
  'nombre' : P.nombre,
  'esFinalizado' : P.esFinalizado,
  'fechaInicio' : P.fechaInicio,
  'partidaid' : P.id
  }
  return HttpResponse(template.render(context, request))

def ponerpieza(request, partidaid):
  template = loader.get_template('JugarPartida/PonerPieza.html')
  partida = Partida.objects.get(pk=partidaid) 
  y = partida.piezaEnJuego

  if (y < 10):
    pieza ='0' + str(y) 
  else :
    pieza = str(y)
  context = {
  'PiezaAPoner' : pieza,
  'partidaid' : partidaid
  }
  return HttpResponse(template.render(context, request))

def rotarpieza(request,partidaid, rotsentido , imagen):
  print imagen
  im = Image.open( "JugarPartida/static/JugarPartida/" + imagen + ".png")
  im.load()

  if rotsentido == 'izq' :
    im = im.rotate(90, 0, 0)
  else :
    im = im.rotate(270, 0, 0)

  im.save("JugarPartida/static/JugarPartida/" + imagen + ".png")
  template = loader.get_template('JugarPartida/PonerPieza.html')
    
  context = {
  'PiezaAPoner' : imagen,
  'partidaid' : partidaid
  }
  return HttpResponse(template.render(context, request))

