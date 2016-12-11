from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Partida(models.Model):
	""" Partida """
	owner = models.ForeignKey(User, null=True)
	jugador2 = models.CharField(max_length=15, null=True, default='Vacio')
	jugador3 = models.CharField(max_length=15, null=True, default='Vacio')
	jugador4 = models.CharField(max_length=15, null=True, default='Vacio')
	jugador5 = models.CharField(max_length=15, null=True, default='Vacio')
	

class Mapa(models.Model):

	uno = models.FilePathField(path="../piezas", match="vacio.png", recursive=True)
	dos = models.FilePathField(path="../piezas", match="vacio.png", recursive=True)
	tres = models.FilePathField(path="../piezas", match="vacio.png", recursive=True)
	cuatro = models.FilePathField(path="../piezas", match="vacio.png", recursive=True)
	cinco = models.FilePathField(path="../piezas", match="inicio.png", recursive=True)
	seis= models.FilePathField(path="../piezas", match="vacio.png", recursive=True)
	siete = models.FilePathField(path="../piezas", match="vacio.png", recursive=True)
	ocho = models.FilePathField(path="../piezas", match="vacio.png", recursive=True)
	nueve = models.FilePathField(path="../piezas", match="vacio.png", recursive=True)

