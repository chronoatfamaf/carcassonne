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


