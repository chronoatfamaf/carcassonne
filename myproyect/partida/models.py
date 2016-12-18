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
	pieza_en_juego = models.IntegerField(default = 10)
 
class Pieza(models.Model):
	# una pieza pertenece a un unico mapa
	# se instancian 72 objetos unicos de pieza en cada partida, cada una con una imagen propia
	# copiada de una imagen en un directorio que no se puede modificar
	# los giros de la imagen simplemente hacen girar a la imagen del directorio de la pieza de la partida
	# ej: static/piezas tiene las piezas 00.png a 71.png y son fijas para todos
	# se crean simultaneamente partida A, partida B entonces se crean static/partida(idpartida=a) 
	# static/partida(idpartida=b) y cada uno de estos directorios con una copia de cada imagen de las imagenes
	# en static/piezas
	# entonces partida A modifica sus propias imagenes, y lo mismo partida b, por lo que no se entra en conflicto
	# una vez finalizadas las partidas, se eliminan todos los directorios donde las partidas guardaban las imagenes
	# no hace falta guardar un atributo para cantidad de giros, por que se gira en la view jugar_partida con la funcion
	# a implementar girar, y se guarda la imagen el path correspondiente ya girada (se sobre escribe el nombre)
	partida = models.ForeignKey( Partida, on_delete=models.CASCADE, blank=True, null=True)
	pathimagen =  models.CharField(max_length=9, unique = True)
	pos_x = models.IntegerField( default=1)
	pos_y = models.IntegerField( default=1)
	# atributos del juego, podrian faltar 
	numLadoAsociado = models.IntegerField(default=0)
	esDescartada = models.BooleanField(default =False)
	#			 ___1___
	#			 |     |
	# pieza =   4|     |2
	#			 |_____|
	#			    3
	lado1 = models.CharField(max_length=50)
	lado2 = models.CharField(max_length=50)
	lado3 = models.CharField(max_length=50)
	lado4 = models.CharField(max_length=50)
	esOcupada = models.BooleanField(default =False)
	nombreDeCelda = models.IntegerField(default = 1, unique = True)

	@classmethod
	def create(x,y,path,partida):
		nueva_pieza = Pieza(partida=partida,pos_x=x,pos_y=y,pathimagen=path)
		return nueva_pieza