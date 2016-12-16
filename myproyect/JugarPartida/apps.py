from django.apps import AppConfig
from .models import Partida, Pieza


class JugarpartidaConfig(AppConfig):
    name = 'JugarPartida'

def compatibilidadaux(piezaAponer, piezafija):



# piezaAponer celdafija son primary key. celdaLibre es un string sacado de la url. lo mismo
# para piezaAponer
def compatibilidad(piezaAponer, celdaLibre):
    pieza = Pieza.objects.get(pk=piezaAponer)
    celda = Celda.objects.get(pk=celdaLibre)
    # si hay error en algun cambio, en la funcion leerarchivo de la vista de inclustrarpieza
    # entonces agregar un if, que chequee si el campo es ocupado de el objeto celda es v o f
    cnombre = celda.nombreDeCelda
    if(cnombre == 1):
        d = Celda.objects.get(pk=(cnombre + 1))
        if (d.esOcupado == True):
            dpieza = Pieza.objects.get(pk=d.piezaid)
            compatib = compatibilidadaux(piezaAponer, dpieza)

        ab = Celda.objects.get(pk=(cnombre + 20))
        if (ab.esOcupado == True):
            abpieza = Pieza.objects.get(pk=ab.piezaid)
            compatib = compatibilidadaux(piezaAponer, abpieza) and compatib
        
        return compatib
    
    elif(cnombre ==20):
   
    elif(cnombre == 381):
  
    elif(cnombre ==400):
    
    else:
     pass


    if (cnombre%20==0):

    elif ((cnombre - 1)%20==0):
  
    elif (cnombre<= 382 and  399 <= cnombre  ):

   elif  ( 2 <= cnombre  and cnombre<= 19):      
 
   else:
     pass
    
