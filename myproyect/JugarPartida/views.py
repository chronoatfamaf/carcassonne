from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import os
from django.utils import timezone
from django.contrib.auth import authenticate, login
from PIL import Image
from .models import Partida, Jugador, Pieza, Celda


ListaDeDescipcionDePiezas = [
                             [ 
                              'Granja',
                              'Granja',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],

                             [ 
                              'Granja',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Granja',
                             ],
                              [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                             ],
                              [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Granja',
                              'Ciudad',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Ciudad',
                              'Ciudad',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Granja',
                             ],
                              [
                              'Ciudad',
                              'Ciudad',
                              'Camino',
                              'Ciudad',
                             ],
                              [
                              'Ciudad',
                              'Ciudad',
                              'Camino',
                              'Ciudad',
                             ],
                              [
                              'Ciudad',
                              'Ciudad',
                              'Camino',
                              'Ciudad',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Granja',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Camino',
                              'Camino',
                             ],      
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Ciudad',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ], 
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ], 
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ], 
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ], 
                             [ 
                              'Granja',
                              'Granja',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Granja',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Granja',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Granja',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Camino',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Camino',
                              'Granja',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Camino',
                              'Granja',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Granja',
                              'Camino',
                              'Camino',
                              'Camino',
                             ],  
                             [ 
                              'Granja',
                              'Camino',
                              'Camino',
                              'Camino',
                             ],   
                             [ 
                              'Granja',
                              'Camino',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Ciudad',
                              'Camino',
                              'Camino',
                              'Camino',
                             ],       
                             [ 
                              'Ciudad',
                              'Camino',
                              'Camino',
                              'Camino',
                             ],
                             [ 
                              'Camino',
                              'Camino',
                              'Camino',
                              'Camino',
                             ],
]





def compatibilidadaux(piezaAponer, piezafija, posiciondepiezaexistente):
  b = False
  pieza1 = Pieza.objects.get(pk=piezaAponer)
  pieza2 = Pieza.objects.get(pk=piezafija)

  if(posiciondepiezaexistente == 'izquierda'):
    if pieza1.lado4 == pieza2.lado2:
        b = True

  if(posiciondepiezaexistente == 'derecha'):
    if pieza1.lado2 == pieza2.lado4:
        b = True

  if(posiciondepiezaexistente == 'abajo'):
    if pieza1.lado3 == pieza2.lado1:
        b = True

  if(posiciondepiezaexistente == 'arriba'):
    if pieza1.lado1 == pieza2.lado3:
        b = True

  return b

# piezaAponer celdafija son primary key. celdaLibre es un string sacado de la url. lo mismo
# para piezaAponer
def compatibilidad(piezaAponer, celdaLibre):
    pieza = Pieza.objects.get(pk=piezaAponer)
    celda = Celda.objects.get(pk=celdaLibre)


    # si hay error en algun cambio, en la funcion leerarchivo de la vista de inclustrarpieza
    # entonces agregar un if, que chequee si el campo es ocupado de el objeto celda es v o f
    cnombre = celda.nombreDeCelda  # nombreDeCelda es el id de la posicion del mapa
    compatib = True
    if(cnombre == 1):
        d = Celda.objects.get(pk=(cnombre + 1))
        ab = Celda.objects.get(pk=(cnombre + 20))

        if ((d.esOcupada == False) and (ab.esOcupada == False)):
         return False

        if (d.esOcupada == True):
            dpieza = Pieza.objects.get(pk=(d.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, dpieza.id, 'derecha') and compatib

        if (ab.esOcupada == True):
            abpieza = Pieza.objects.get(pk=(ab.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, abpieza.id, 'abajo') and compatib
        
        # return compatib lo comentemos
    elif(cnombre == 20):
        i = Celda.objects.get(pk=(cnombre - 1))
        ab = Celda.objects.get(pk=(cnombre + 20))

        if ((i.esOcupada == False) and (ab.esOcupada == False)):
         return False


        if (i.esOcupada == True):
            pieza = Pieza.objects.get(pk=(i.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, ipieza.id, 'izquierda')

        if (ab.esOcupada == True):
            abpieza = Pieza.objects.get(pk=(ab.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, abpieza.id, 'abajo') and compatib   
    elif(cnombre == 381):
        d = Celda.objects.get(pk=(cnombre + 1))
        ar = Celda.objects.get(pk=(cnombre - 20))

        if ((d.esOcupada == False) and (ar.esOcupada == False)):
         return False

        if (d.esOcupada == True):
            dpieza = Pieza.objects.get(pk=(d.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, dpieza.id, 'derecha') and compatib

        if (ar.esOcupada == True):
            arpieza = Pieza.objects.get(pk=(ar.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, arpieza.id, 'arriba') and compatib
    elif(cnombre ==400):
        i = Celda.objects.get(pk=(cnombre - 1))
        ar = Celda.objects.get(pk=(cnombre - 20))

        if ((i.esOcupada == False) and (ar.esOcupada == False)):
         return False

        if (i.esOcupada == True):
            ipieza = Pieza.objects.get(pk=(i.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, ipieza.id, 'izquierda')

        if (ar.esOcupada == True):
            abpieza = Pieza.objects.get(pk=(ar.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, arpieza.id, 'arriba') and compatib
    else:
        pass

    if (cnombre%20==0 and cnombre!=20 and cnombre!=400):
        i = Celda.objects.get(pk=(cnombre - 1))
        ar = Celda.objects.get(pk=(cnombre - 20))
        ab = Celda.objects.get(pk=(cnombre + 20))

        if ((i.esOcupada == False) and (ab.esOcupada == False) and (ar.esOcupada == False)):
         return False


        if (i.esOcupada == True):
            ipieza = Pieza.objects.get(pk=(i.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, ipieza.id, 'izquierda')
        if (ar.esOcupada == True):
            arpieza = Pieza.objects.get(pk=(ar.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, arpieza.id, 'arriba') and compatib
        if (ab.esOcupada == True):
            abpieza = Pieza.objects.get(pk=(ab.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, abpieza.id, 'abajo') and compatib 
        
    elif ((cnombre - 1)%20==0 and cnombre!=1 and cnombre!=381):
        d = Celda.objects.get(pk=(cnombre - 1))
        ar = Celda.objects.get(pk=(cnombre - 20))
        ab = Celda.objects.get(pk=(cnombre + 20))

        if ((d.esOcupada == False) and (ab.esOcupada == False) and (ar.esOcupada == False)):
          return False

        if (d.esOcupada == True):
            dpieza = Pieza.objects.get(pk=(d.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, dpieza.id, 'derecha') and compatib
        if (ar.esOcupada == True):
            arpieza = Pieza.objects.get(pk=(ar.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, arpieza.id, 'arriba') and compatib
        if (ab.esOcupada == True):
            abpieza = Pieza.objects.get(pk=(ab.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, abpieza.id, 'abajo') and compatib 

    elif (cnombre >= 382 and  cnombre <= 399):
        d = Celda.objects.get(pk=(cnombre + 1))
        i = Celda.objects.get(pk=(cnombre - 1))
        ar = Celda.objects.get(pk=(cnombre - 20))

        if ((i.esOcupada == False) and (d.esOcupada == False) and (ar.esOcupada == False)):
           return False
        if (d.esOcupada == True):
            dpieza = Pieza.objects.get(pk=(d.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, dpieza.id, 'derecha') and compatib
        if (i.esOcupada == True):
            ipieza = Pieza.objects.get(pk=(i.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, ipieza.id, 'izquierda') and compatib
        if (ar.esOcupada == True):
            arpieza = Pieza.objects.get(pk=(ar.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, arpieza.id, 'arriba') and compatib

    elif  (cnombre >= 2 and cnombre <= 19):
        d = Celda.objects.get(pk=(cnombre + 1))
        i = Celda.objects.get(pk=(cnombre - 1))
        ab = Celda.objects.get(pk=(cnombre + 20))
  
        if((i.esOcupada == False) and (ab.esOcupada == False) and (d.esOcupada == False)):
           return False

        if (d.esOcupada == True):
            dpieza = Pieza.objects.get(pk=(d.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, dpieza.id, 'derecha') and compatib
        if (i.esOcupada == True):
            ipieza = Pieza.objects.get(pk=(i.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, ipieza.id, 'izquierda') and compatib
        if (ab.esOcupada == True):
            abpieza = Pieza.objects.get(pk=(ab.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, abpieza.id, 'abajo') and compatib
    else:

        d = Celda.objects.get(pk=(cnombre + 1))
        ab = Celda.objects.get(pk=(cnombre + 20))
        i = Celda.objects.get(pk=(cnombre - 1))
        ar = Celda.objects.get(pk=(cnombre - 20))
        if ((i.esOcupada == False) and (ab.esOcupada == False) and (ar.esOcupada == False)
            and (d.esOcupada == False)):
           return False

        if (d.esOcupada == True):
            dpieza = Pieza.objects.get(pk=(d.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, dpieza.id, 'derecha') and compatib 
        if (i.esOcupada == True):
            ipieza = Pieza.objects.get(pk=(i.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, ipieza.id, 'izquierda') and compatib
        if (ar.esOcupada == True):
            arpieza = Pieza.objects.get(pk=(ar.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, arpieza.id, 'arriba') and compatib
        if (ab.esOcupada == True):
            abpieza = Pieza.objects.get(pk= (ab.piezaid).id)
            compatib = compatibilidadaux(piezaAponer, abpieza.id, 'abajo') and compatib

        return compatib



def crearpartida(request):
  template = loader.get_template('JugarPartida/CrearPartida.html')
  context = {}
  return HttpResponse(template.render(context, request))

def partidacreada(request):
  nombreJugadores = ['Mateo', 'Juan', 'Pedro', 'Marcos', 'Esteban']
  cantJug = int(request.POST.get('numerodejugadores', '0'))
  for x in xrange(0, cantJug):
    J = Jugador(nombre=nombreJugadores[x])
    J.save()

  #cargo las celdas
  for y in xrange(1, 400):
    if (y < 10):
      celda = Celda(imagenPieza = '00' + str(y), nombreDeCelda = y)
    elif (y < 100 and y >= 10):
      celda = Celda(imagenPieza = '0' + str(y), nombreDeCelda = y)
    else:
      celda = Celda(imagenPieza=str(y), nombreDeCelda = y)
    celda.save() 

  # Cargo las piezas
  for x in xrange(1, 72):
    if x < 10:
      piezanueva = Pieza(esDescartada=False,
                         lado1 = ListaDeDescipcionDePiezas[x - 1][0],
                         lado2 = ListaDeDescipcionDePiezas[x - 1][1],
                         lado3 = ListaDeDescipcionDePiezas[x - 1][2],
                         lado4 = ListaDeDescipcionDePiezas[x - 1][3],
                         imagenAsociada ='0' + str(x) + '.png' )
    else :
      piezanueva = Pieza(esDescartada=False,
                         lado1 = ListaDeDescipcionDePiezas[x - 1][0],
                         lado2 = ListaDeDescipcionDePiezas[x - 1][1],
                         lado3 = ListaDeDescipcionDePiezas[x - 1][2],
                         lado4 = ListaDeDescipcionDePiezas[x - 1][3],
                         imagenAsociada = str(x) + '.png' )
    piezanueva.save()
  P = Partida(nombre = request.POST['nombre'],
                fechaInicio = str(timezone.now()), esFinalizado = 'N', piezaEnJuego=1)
  P.save()
  template = loader.get_template('JugarPartida/PartidaCreada.html')

  piezaenjuego = P.piezaEnJuego

  if (piezaenjuego < 10):
    PiezaAPoner ='0' + str(piezaenjuego) 
  else :
    PiezaAPoner = str(piezaenjuego)

# Utiliza la funcion os.getcwd() para recuperar el directorio de trabajo actual
# os.chdir('direccion nueva de directorio') sirve paracambiar el directiorio de trabajo actual

# Esta modificacion servira para el juego multipartida
#
# try:
#   existe=opendirectorio???( "JugarPartida/static/JugarPartida/" + str(P.id) + "/" + "idmapapieza +
#     ".png")
# except IOError :
#    creamos aca el directorio por defecto con nombre "idPartida"
#    os.makedirs("JugarPartida/static/JugarPartida/" + str(P.id))
#
#
#  try:
#    existe =  Image.open( "JugarPartida/static/JugarPartida/" + str(P.id) + "/" + "idmapapieza +
#     ".png")
#  except IOError :
#    im = Image.open( "JugarPartida/static/JugarPartida/ImagBasic/" + PiezaAPoner + ".png")
#    im.save("JugarPartida/static/JugarPartida/" +str(P.id) + "/" + PiezaAPoner + ".png")
#  else:
#     pass
#



  im = Image.open( "JugarPartida/static/JugarPartida/" + PiezaAPoner + ".png")
  im.load()
  # Modificar segun el numero de columnas o filas que se tenga 
  CeldaDelCentroDelMapa = '190'
  im.save("JugarPartida/static/JugarPartida/" + CeldaDelCentroDelMapa + ".png")  
  CeldaCentral = Celda.objects.get(pk=CeldaDelCentroDelMapa)
  CeldaCentral.esOcupada = True
  CeldaCentral.piezaid = Pieza.objects.get(pk=P.piezaEnJuego)
  CeldaCentral.save()
  P.piezaEnJuego = P.piezaEnJuego + 1
  P.save()
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

# Esta modificacion servira para el juego multipartida
#  try:
#    existe =  Image.open( "JugarPartida/static/JugarPartida/" + str(P.id) + "/" + "imagen +
#     ".png")
#  except IOError :
#    im = Image.open( "JugarPartida/static/JugarPartida/ImagBasic/" + imagen + ".png")
#    im.save("JugarPartida/static/JugarPartida/" +str(P.id) + "/" + imagen + ".png")
#    im = Image.open( "JugarPartida/static/JugarPartida/" + str(P.id) + "/" + imagen + ".png")
#  else:
#     pass
#

# La linea de aca abajo la debemos borrar  al hacer al juego mutipartida 
  im = Image.open( "JugarPartida/static/JugarPartida/" + imagen + ".png")
  im.load()
  piezadelturno = Pieza.objects.get(pk=imagen)
  if rotsentido == 'izq' :
    im = im.rotate(90, 0, 0)
    aux1 = piezadelturno.lado4
    aux2 = piezadelturno.lado2
    piezadelturno.lado2 = piezadelturno.lado3
    piezadelturno.lado3 = aux1
    piezadelturno.lado4 = piezadelturno.lado1
    piezadelturno.lado1 =  aux2
  else :
    aux1 = piezadelturno.lado2
    aux2 = piezadelturno.lado3
    piezadelturno.lado2 = piezadelturno.lado1
    piezadelturno.lado3 = aux1
    piezadelturno.lado1 = piezadelturno.lado4
    piezadelturno.lado4 = aux2
    im = im.rotate(270, 0, 0)

  im.save("JugarPartida/static/JugarPartida/" + imagen + ".png")
  template = loader.get_template('JugarPartida/PonerPieza.html')
    
  context = {
  'PiezaAPoner' : imagen,
  'partidaid' : partidaid
  }
  return HttpResponse(template.render(context, request))


def ponerseguidor(request, partidaid , imagen):

# Esta modificacion servira para el juego multipartida
#  try:
#    existe =  Image.open( "JugarPartida/static/JugarPartida/" + str(P.id) + "/" + "imagen +
#     ".png")
#  except IOError :
#    im = Image.open( "JugarPartida/static/JugarPartida/ImagBasic/" + imagen + ".png")
#    im.save("JugarPartida/static/JugarPartida/" +str(P.id) + "/" + imagen + ".png")
#    im = Image.open( "JugarPartida/static/JugarPartida/" + str(P.id) + "/" + imagen + ".png")
#  else:
#     pass
#

# La linea de aca abajo la debemos borrar  al hacer al juego mutipartida 
  im = Image.open( "JugarPartida/static/JugarPartida/" + imagen + ".png")
  im.load()
  piezadelturno = Pieza.objects.get(pk=imagen)
  if rotsentido == 'izq' :
    im = im.rotate(90, 0, 0)
    aux1 = piezadelturno.lado4
    aux2 = piezadelturno.lado2
    piezadelturno.lado2 = piezadelturno.lado3
    piezadelturno.lado3 = aux1
    piezadelturno.lado4 = piezadelturno.lado1
    piezadelturno.lado1 =  aux2
  else :
    aux1 = piezadelturno.lado2
    aux2 = piezadelturno.lado3
    piezadelturno.lado2 = piezadelturno.lado1
    piezadelturno.lado3 = aux1
    piezadelturno.lado1 = piezadelturno.lado4
    piezadelturno.lado4 = aux2
    im = im.rotate(270, 0, 0)

  im.save("JugarPartida/static/JugarPartida/" + imagen + ".png")
  template = loader.get_template('JugarPartida/PonerPieza.html')
    
  context = {
  'PiezaAPoner' : imagen,
  'partidaid' : partidaid
  }
  return HttpResponse(template.render(context, request))




def incrustarpieza(request, partidaid, idmapapieza , imagen):
  context = {}   
  celdaLibre = idmapapieza
  partida = Partida.objects.get(pk=partidaid) 
  template = loader.get_template('JugarPartida/PonerPieza.html')


  if (compatibilidad(imagen, celdaLibre) == False):
    context ['PiezaAPoner'] = imagen
    context ['partidaid'] = partidaid
    context['AnuncioDeError'] = 'Elija una celda que este al lado de otra celda que tenga una pieza depositada encima o que sea compatible con los lados en los que ambas se conectan'
    return HttpResponse(template.render(context, request))
   

# Esta modificacion servira para el juego multipartida
#  try:
#    existe =  Image.open( "JugarPartida/static/JugarPartida/" + str(P.id) + "/" + "imagen +
#     ".png")
#  except IOError :
#    im = Image.open( "JugarPartida/static/JugarPartida/ImagBasic/" + imagen + ".png")
#    im.save("JugarPartida/static/JugarPartida/" +str(P.id) + "/" + imagen + ".png")
#    im = Image.open( "JugarPartida/static/JugarPartida/" + str(P.id) + "/" + imagen + ".png")
#  else:
#     pass
#

# La linea de aca abajo la debemos borrar  al hacer al juego mutipartida 

  im = Image.open( "JugarPartida/static/JugarPartida/" +imagen + ".png")
  im.load()

  # cambiar por un "for" que itere en la tabla de piezas para buscar el nombre de 
  # imagen , si es que se repite ya que es unico dicho nombre
  try:
    existe =  Image.open( "JugarPartida/static/JugarPartida/" + idmapapieza + ".png")
  except IOError :
    im.save("JugarPartida/static/JugarPartida/" + idmapapieza + ".png")
    celdareceptora = Celda.objects.get(pk=celdaLibre)
    celdareceptora.esOcupada = True
    celdareceptora.piezaid = Pieza.objects.get(pk=partida.piezaEnJuego)
    celdareceptora.save()  
    partida.piezaEnJuego = partida.piezaEnJuego + 1
  else:
    context['AnuncioDeError'] = 'Elija una celda libre para depositar la pieza'
  y = partida.piezaEnJuego
  partida.save()
  

  if y < 10:
    pieza ='0' + str(y) 
  else :
    pieza = str(y)

  context ['PiezaAPoner'] = pieza
  context ['partidaid'] = partidaid
  return HttpResponse(template.render(context, request))
