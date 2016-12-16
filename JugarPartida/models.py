from __future__ import unicode_literals
from django.db import models


tipoSeguidores = ["caballero", "ladron", "granjero", "monje"]
tipoLado = ["ciudades", "caminos", "campos", "claustros"]

class Jugador(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    puntaje = models.IntegerField(default=0)
    ranking = models.IntegerField(default=0)
    posicion = models.IntegerField(default=0)


class Mapa(models.Model):
    numeroJugadores = models.IntegerField(default = 1, unique = True)
    turnoPartida = models.IntegerField(default = 1)
    ListasDePiezas = []


class Celda(models.Model):
    imagenPieza = models.CharField(default='N', max_length=20)
    esOcupada = models.BooleanField()
    # piezaid = models.ForeignKey("Pieza", on_delete=models.CASCADE)
    nombreDeCelda = models.IntegerField(default = 1, unique = True)


class Partida(models.Model):
    nombre = models.CharField(max_length=200)
    esFinalizado = models.CharField(max_length=1)
    fechaInicio = models.CharField(max_length=50)
    esTurno = models.IntegerField(default=1)
    piezaEnJuego = models.IntegerField(default=1)
    #fechaFin = models.CharField(max_length=20)
    #jugadorInicial = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Pieza(models.Model):
    numLadoAsociado = models.IntegerField(default=0)
    esDescartada = models.BooleanField()
    # lado1 = models.CharField(max_length=50)
    # lado2 = models.CharField(max_length=50)
    # lado3 = models.CharField(max_length=50)
    # lado4 = models.CharField(max_length=50)
    cantRotacion = models.IntegerField(default=0)
#    Usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    imagenAsociada =  models.CharField(max_length=9, unique = True)
    # Es posible usar lo siguiente
    # conEscudo = models.BooleanField()
    # conClaustro = models.BooleanField()
    #tipoDeSeguidores = models.CharField(max_length=50)


class Terreno(models.Model):
    idNombreTerreno = models.IntegerField(default=0, unique = True)
    esOcupado = models.BooleanField()
    asocPieza = models.ForeignKey("Pieza")

class Camino(Terreno):
    esTe = models.BooleanField()
    ladoLibre = models.IntegerField(default=-1)
    esCruce = models.BooleanField()
    ladoInicio = models.IntegerField(default=-1)
    ladoFinal = models.IntegerField(default=-1)

class Ciudad(Terreno):
    numeroEscudos = models.IntegerField(default=-1)
    esTodoCiudad = models.BooleanField()
    ladoInicio = models.IntegerField(default=-1)
    ladoFinal = models.IntegerField(default=-1)
    unicoLadoLibre = models.IntegerField(default=-1)
    unicoLadoCiudad = models.IntegerField(default=-1)

class Granja(Terreno):
    conClaustro = models.BooleanField()
    claustroOcupado = models.BooleanField()
    ladoInicio = models.IntegerField(default=-1)
    ladoFinal = models.IntegerField(default=-1)
    unicoLadoLibre = models.IntegerField(default=-1)
    unicoLadoGranja = models.IntegerField(default=-1)
    esTodoGranja = models.BooleanField()
    esquinaLibre = models.IntegerField(default=-1)
