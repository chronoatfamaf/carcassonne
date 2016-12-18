import glob
import PIL
from django.db import models
from partida.models import *

# dado un numero entre 0 y 71 (que identifica una imagen de pieza)
# se devuelve los lados que tiene esa pieza
# ej lados(57) = [1,1,1,2] signgifica que 
# 57.png el lado1 lado2 y lado3 son tipo 1 y el lado4 tipo 2
# en ejemplo de tipos serian 1 para camino, 2 para castillo, 3 granja y asi
# la hice  con un solo caso, y con un significado cualquiera solo a modo de ejemplo
# del valor de los lados
def lados_pieza(pieza_en_juego):
	lados = []
	if pieza_en_juego == 1:
		lados = [1,1,3,2]
	else:
		lados = [3,3,2,1]
	return lados		

			
# POST: devuelve 1 si la pieza_a_poner se puede poner donde quiso el jugador,
# sino 0
# PRE: no hay ninguna pieza en la posicion donde el usuario quiere poner esta pieza
# y la posicion pertenece a la matriz, es decir (ej: si la matriz es 4x4 el usuario ingreso x,y
# tal que 0 =< x  < 4,  lo mismo con y 	
#			 ___1___
#			 |     |
# pieza =   4|     |2
#			 |_____|
#			    3
#			
def compatibilidad_juego(x,y,lados, partida):
	# lados
	lado1 = lados[0]
	lado2 = lados[1]
	lado3 = lados[2]
	lado4 = lados[3]
	# flags para controlar que es valido poner la ficha
	arriba_valido = 0
	abajo_valido = 0
	derecha_valido = 0
	izquierda_valido = 0
	# obtenemos todas las piezas jugadas
	piezas_partida = Pieza.objects.get(partida=partida)
	pieza_arriba = piezas_partida.filter(pos_x=pos_x+1,pos_y=pos_y)
	pieza_abajo = piezas_partida.filter(pos_x=pos_x-1,pos_y=pos_y)
	pieza_derecha = piezas_partida.filter(pos_x=pos_x,pos_y=pos_y+1)
	pieza_izquierda = piezas_partida.filter(pos_x=pos_x,pos_y=pos_y+1)

	# si no hay pieza arriba
	if not pieza_arriba:
		arriba_valido = 1
	else: 
		if lado1 == pieza_arriba.lado3:
			arriba_valido = 1
	if not pieza_abajo:
		abajo_valido = 1
	else: 
		if lado3 == pieza_abajo.lado1:
			abajo_valido = 1
	if not pieza_derecha:
		derecha_valido = 1
	else: 
		if lado2 == pieza_derecha.lado4:
			derecha_valido = 1
	if not pieza_izquierda:
		izquierda_valido = 1
	else: 
		if lado4 == pieza_izquierda.lado2:
			izquierda_valido = 1


	if arriba_valido and abajo_valido and derecha_valido and izquierda_valido:
		return 1
	else:
		return 0

def agregar_lados_a_pieza(pieza,lados):
	pieza.lado1 = lados[0]
	pieza.lado1 = lados[1]
	pieza.lado1 = lados[2]
	pieza.lado1 = lados[3]

	return pieza

def removerdirectorio(nombredirectorio):
    imagenesbasicas = glob.glob("../static/piezas/")
    try:
      # Intentamos listar los elementos del directorio Partida1 por ejemplo
      # sin lo logramos es que no existe el directorio y por lo tano lo creamos 
      listadeimagenes = glob.glob(nombredirectorio)
    except OSError:
      os.makedirs(("../static/" + str(nombredirectorio)))    
      for x in xrange(1, 72):
        im = Image.open("../static/piezas/" + PiezaAPoner + ".png")
        im.save("../static/partida" + str(nombredirectorio) + "/" +
                 imagenesbasicas[x - 1])

    if(listadeimagenes == []):
      os.rmdir(("../static/partida" + str(nombredirectorio)))
      os.makedirs(("../static/partida" + str(nombredirectorio)))    
      for x in xrange(1, 72):
        im = Image.open("../static/piezas/" + 
                        imagenesbasicas[x - 1])
        im.save("../static/partida" + str(nombredirectorio) + "/" +
                 imagenesbasicas[x - 1])

