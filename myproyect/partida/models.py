from django.db import models

# Create your models here.

class Partida(models.Model):
	""" Partida """
	# la cantidad de jugadores que jugaran la partida, (un numero entre 2 y 5)
	cantidad_jugadores = models.IntegerField( default=2)
	# la cantidad de jugadores jugando (es decir los que estan en la partida modo de espera)
	# cuando jugando = cantidad_jugadores, la partida i.e juego comienza
	# default uno porque el usuario que crea la partida la juega tambien
	jugando = models.IntegerField( default=1)
	turnos = models.IntegerField(default=1)

class Mapa(models.Model):
	partida = models.ForeignKey(Partida, on_delete=models.CASCADE, blank=True, null=True)

class CeldaMapa(models.Model):
 	imagenPieza = models.CharField(default='N', max_length=20)
 	esOcupada = models.BooleanField()
	mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE, blank=True, null=True)

class Pieza(models.Model):
    numLadoAsociado = models.IntegerField(default=0)
    esDescartada = models.BooleanField()
#    ladoA = models.ForeignKey("Pieza", on_delete=models.CASCADE)
#    ladoB = models.ForeignKey("Pieza", on_delete=models.CASCADE)
#    ladoC = models.ForeignKey("Pieza", on_delete=models.CASCADE)
#    ladoD = models.ForeignKey("Pieza", on_delete=models.CASCADE)
#    Usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    imagenAsociada =  models.CharField(max_length=9, unique = True)	
