from django.apps import AppConfig
from .models import *

class JugarpartidaConfig(AppConfig):
    name = 'JugarPartida'


def compatibilidadaux(piezaAponer, piezafija):
    b = False
    pieza1 = Pieza.objects.get(pk=piezaAponer)
    pieza2 = Pieza.objects.get(pk=piezafija)

    if pieza1.lado1 == pieza2.lado3:
        b = True
    elif pieza1.lado2 == pieza2.lado4:
        b = True
    elif pieza1.lado3 == pieza2.lado1:
        b = True
    elif pieza1.lado4 == pieza2.lado2:
        b = True

    return b

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
    
    elif(cnombre == 20):
        i = Celda.objects.get(pk=(cnombre - 1))
        if (i.esOcupado == True):
            pieza = Pieza.objects.get(pk=i.piezaid)
            compatib = compatibilidadaux(piezaAponer, ipieza)

        ab = Celda.objects.get(pk=(cnombre + 20))
        if (ab.esOcupado == True):
            abpieza = Pieza.objects.get(pk=ab.piezaid)
            compatib = compatibilidadaux(piezaAponer, abpieza) and compatib   
    elif(cnombre == 381):
        d = Celda.objects.get(pk=(cnombre + 1))
        if (d.esOcupado == True):
            dpieza = Pieza.objects.get(pk=d.piezaid)
            compatib = compatibilidadaux(piezaAponer, dpieza)

        ar = Celda.objects.get(pk=(cnombre - 20))
        if (ar.esOcupado == True):
            arpieza = Pieza.objects.get(pk=ar.piezaid)
            compatib = compatibilidadaux(piezaAponer, arpieza) and compatib
    elif(cnombre ==400):
        i = Celda.objects.get(pk=(cnombre - 1))
        if (i.esOcupado == True):
            ipieza = Pieza.objects.get(pk=i.piezaid)
            compatib = compatibilidadaux(piezaAponer, ipieza)

        ar = Celda.objects.get(pk=(cnombre - 20))
        if (ar.esOcupado == True):
            abpieza = Pieza.objects.get(pk=ar.piezaid)
            compatib = compatibilidadaux(piezaAponer, arpieza) and compatib
    else:
        pass

    if (cnombre%20==0 and cnombre!=20 and cnombre!=400):
        i = Celda.objects.get(pk=(cnombre - 1))
        if (i.esOcupado == True):
            ipieza = Pieza.objects.get(pk=i.piezaid)
            compatib = compatibilidadaux(piezaAponer, ipieza)
        ar = Celda.objects.get(pk=(cnombre - 20))
        if (ar.esOcupado == True):
            arpieza = Pieza.objects.get(pk=ar.piezaid)
            compatib = compatibilidadaux(piezaAponer, arpieza) and compatib
        ab = Celda.objects.get(pk=(cnombre + 20))
        if (ab.esOcupado == True):
            abpieza = Pieza.objects.get(pk=ab.piezaid)
            compatib = compatibilidadaux(piezaAponer, abpieza) and compatib 
        
    elif ((cnombre - 1)%20==0 and cnombre!=1 and cnombre!=381):
        d = Celda.objects.get(pk=(cnombre - 1))
        if (d.esOcupado == True):
            dpieza = Pieza.objects.get(pk=d.piezaid)
            compatib = compatibilidadaux(piezaAponer, dpieza)
        ar = Celda.objects.get(pk=(cnombre - 20))
        if (ar.esOcupado == True):
            arpieza = Pieza.objects.get(pk=ar.piezaid)
            compatib = compatibilidadaux(piezaAponer, arpieza) and compatib
        ab = Celda.objects.get(pk=(cnombre + 20))
        if (ab.esOcupado == True):
            abpieza = Pieza.objects.get(pk=ab.piezaid)
            compatib = compatibilidadaux(piezaAponer, abpieza) and compatib 

    elif (cnombre <= 382 and  cnombre >= 399):
        d = Celda.objects.get(pk=(cnombre + 1))
        if (d.esOcupado == True):
            dpieza = Pieza.objects.get(pk=d.piezaid)
            compatib = compatibilidadaux(piezaAponer, dpieza)
        i = Celda.objects.get(pk=(cnombre - 1))
        if (i.esOcupado == True):
            ipieza = Pieza.objects.get(pk=i.piezaid)
            compatib = compatibilidadaux(piezaAponer, ipieza) and compatib
        ar = Celda.objects.get(pk=(cnombre - 20))
        if (ar.esOcupado == True):
            arpieza = Pieza.objects.get(pk=ar.piezaid)
            compatib = compatibilidadaux(piezaAponer, arpieza) and compatib

    elif  ( 2 <= cnombre  and cnombre<= 19):
        d = Celda.objects.get(pk=(cnombre + 1))
        if (d.esOcupado == True):
            dpieza = Pieza.objects.get(pk=d.piezaid)
            compatib = compatibilidadaux(piezaAponer, dpieza)
        i = Celda.objects.get(pk=(cnombre - 1))
        if (i.esOcupado == True):
            ipieza = Pieza.objects.get(pk=i.piezaid)
            compatib = compatibilidadaux(piezaAponer, ipieza) and compatib
        ab = Celda.objects.get(pk=(cnombre + 20))
        if (ab.esOcupado == True):
            abpieza = Pieza.objects.get(pk=ab.piezaid)
            compatib = compatibilidadaux(piezaAponer, abpieza) and compatib
    else:
        d = Celda.objects.get(pk=(cnombre + 1))
        if (d.esOcupado == True):
            dpieza = Pieza.objects.get(pk=d.piezaid)
            compatib = compatibilidadaux(piezaAponer, dpieza)
        i = Celda.objects.get(pk=(cnombre - 1))
        if (i.esOcupado == True):
            ipieza = Pieza.objects.get(pk=i.piezaid)
            compatib = compatibilidadaux(piezaAponer, ipieza) and compatib
        ar = Celda.objects.get(pk=(cnombre - 20))
        if (ar.esOcupado == True):
            arpieza = Pieza.objects.get(pk=ar.piezaid)
            compatib = compatibilidadaux(piezaAponer, arpieza) and compatib
        ab = Celda.objects.get(pk=(cnombre + 20))
        if (ab.esOcupado == True):
            arpieza = Pieza.objects.get(pk=ab.piezaid)
            compatib = compatibilidadaux(piezaAponer, abpieza) and compatib

