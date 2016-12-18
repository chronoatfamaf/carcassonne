from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Jugador(models.Model):
  nombre = models.CharField(max_length=20)
  puntaje = models.IntegerField(default=0)
  ranking = models.IntegerField(default=0)
  posicion = models.IntegerField(default=0)


class Mapa(models.Model):
  numeroJugadores = models.IntegerField(default = 1, unique = True)
  turnoPartida = models.IntegerField(default = 1)
  ListasDeiezas = []
  
class Pieza(models.Model):
    numLadoAsociado = models.IntegerField(default=0)
    esDescartada = models.BooleanField(default =False)
    lado1 = models.CharField(max_length=50)
    lado2 = models.CharField(max_length=50)
    lado3 = models.CharField(max_length=50)
    lado4 = models.CharField(max_length=50)
    numerosDeTerrenos = models.IntegerField(default=1)
    ubicacionSeguidorEnTerreno = models.IntegerField(default=0)
    #Usuario = models.ForeignKey("Jugador", on_delete=models.CASCADE, blank=True ,null=True)
    imagenAsociada =  models.CharField(max_length=9, unique = True)

class Celda(models.Model):
  imagenPieza = models.CharField(default='N', max_length=20)
  esOcupada = models.BooleanField(default =False)
  piezaid = models.ForeignKey(Pieza, on_delete=models.CASCADE, blank=True ,null=True)
  nombreDeCelda = models.IntegerField(default = 1, unique = True)


class Partida(models.Model):
   
   nombre = models.CharField(max_length=200)
   esFinalizado = models.CharField(max_length=1)
   fechaInicio = models.CharField(max_length=50)
   esTurno = models.IntegerField(default=1)
   piezaEnJuego = models.IntegerField(default=1)
   #fechaFin = models.CharField(max_length=20)
   #jugadorInicial = models.ForeignKey(Jugador, on_delete=models.CASCADE, blank=True ,null=True)

class Seguidor(models.Model):
    jugador = models.ForeignKey("Jugador", on_delete=models.CASCADE, blank=True ,null=True)
    terreno = models.ForeignKey("Terreno", on_delete=models.CASCADE, blank=True ,null=True)
    color = models.CharField(max_length=7)


class Terreno(models.Model):
    idNombreTerreno = models.IntegerField(default=0)
    esOcupado = models.BooleanField(default=False)
    asocPieza = models.ForeignKey("Pieza", blank=True ,null=True)
    numeroDePosicionEnPieza = models.IntegerField(default=0)

class Camino(Terreno):
    esTe = models.BooleanField()
    ladoLibre = models.IntegerField(default=0)
    esCruce = models.BooleanField()
    ladoInicio = models.IntegerField(default=0)
    ladoSeccionInicio  = models.IntegerField(default=0)
    ladoFinal = models.IntegerField(default=0)
    ladoSeccionFinal = models.IntegerField(default=0)
    
class Ciudad(Terreno):
    numeroEscudos = models.IntegerField(default=0)
    esTodoCiudad = models.BooleanField()
    ladoInicio = models.IntegerField(default=0)
    ladoSeccionInicio  = models.IntegerField(default=0)
    ladoFinal = models.IntegerField(default=0)
    ladoSeccionFinal = models.IntegerField(default=0)
    unicoLadoLibre = models.IntegerField(default=0)
    unicoLadoCiudad = models.IntegerField(default=0)

class Granja(Terreno):
    conClaustro = models.BooleanField()
    claustroOcupado = models.BooleanField()
    ladoInicio = models.IntegerField(default=0)
    ladoSeccionInicio  = models.IntegerField(default=0)
    ladoFinal = models.IntegerField(default=0)
    ladoSeccionFinal = models.IntegerField(default=0)
    unicoLadoLibre = models.IntegerField(default=0)
    unicoLadoGranja = models.IntegerField(default=0)
    esTodoGranja = models.BooleanField()
    esquinaLibre = models.IntegerField(default=0)
