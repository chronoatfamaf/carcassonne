from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pieza(models.Model):

	nombre = models.CharField(max_length=15, default='Vacio')
	path = models.CharField(max_length=50, default = '../../../static/piezas/vacio.png')
	lado0 = models.CharField(max_length=15, default="Vacio")
	lado1 = models.CharField(max_length=15, default="Vacio")
	lado2 = models.CharField(max_length=15, default="Vacio")
	lado3 = models.CharField(max_length=15, default="Vacio")
	seguidor = models.BooleanField(default=False)
	donde_esta_el_seguidor = models.CharField(max_length=15, default='Vacio')#Granja, Ciudad, etc

	def __string__(self):
		return str(self.nombre)

class Mapa(models.Model):

	p1 = models.ForeignKey(Pieza, default=1, related_name='p1_content_type')
	p2 = models.ForeignKey(Pieza, default=1, related_name='p2_content_type')
	p3 = models.ForeignKey(Pieza, default=1, related_name='p3_content_type')
	p4 = models.ForeignKey(Pieza, default=1, related_name='p4_content_type')
	p5 = models.ForeignKey(Pieza, default=1, related_name='p5_content_type')
	p6 = models.ForeignKey(Pieza, default=1, related_name='p6_content_type')
	p7 = models.ForeignKey(Pieza, default=1, related_name='p7_content_type')
	p8 = models.ForeignKey(Pieza, default=1, related_name='p8_content_type')
	p9 = models.ForeignKey(Pieza, default=1, related_name='p9_content_type')


class Partida(models.Model):
	""" Partida """
	owner = models.ForeignKey(User, null=True, related_name='owner')
	jugador2 = models.ForeignKey(User, null=True, related_name='j2')
	jugador3 = models.ForeignKey(User, null=True, related_name='j3')
	jugador4 = models.ForeignKey(User, null=True, related_name='j4')
	jugador5 = models.ForeignKey(User, null=True, related_name='j5')
	cantjugadores = models.IntegerField(default=1)
	totaljugadores = models.IntegerField(default=2)
	mapa = models.ForeignKey(Mapa, default=1)









