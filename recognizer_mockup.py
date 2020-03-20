# Reconocimiento de condensadores en imágenes de circuitos impresos.

import numpy as np
import cv2
import random

def reconocer_imagen (imagen_entrada):
    if type(imagen_entrada) is str:
        imagen_entrada = cv2.imread(imagen_entrada)
    #cv2.imshow('Imagen', imagen_entrada)
    #cv2.waitKey(0)

    """
     
     Una vez cargada la imagen se ejecuta un
     código capaz de reconocer si la imagen es apta para ser reconocida 
     por el algoritmo que cuenta el número de condensadores de la misma.
     Finalmente se devuelve un resultado 'res' que dictamina si la imagen
     es válida o no.
     
    """

    #res = 'Esta imagen NO es un circuito impreso'
    res = 'Esta imagen SÍ es un circuito impreso y puede reconocerse'
    return res

def contar_condensadores (imagen_entrada):
    if type(imagen_entrada) is str:
        imagen_entrada = cv2.imread(imagen_entrada)

    #cv2.imshow('Imagen', imagen_entrada)
    #cv2.waitKey(0)

    """
    
    Esta función va a contar el número de condensadores que hay dentro de la imagen.
    Una vez calculado, devolverá un resultado, 'res', donde habrá un entero que indique
    cuántos condensadores hay.
    
    """
    res = random.randrange(20) # Por el momento se da un valor aleatorio.

    return res

def posicionar_condensadores (imagen_entrada):
    if type(imagen_entrada) is str:
        imagen_entrada = cv2.imread(imagen_entrada)
    cv2.imshow('Imagen', imagen_entrada)
    #cv2.waitKey(0)
    """

    En este apartado se marcará el centro radial de cada condensador.

    """
    res = [random.randrange(1000), random.randrange(1000)]  # Por el momento se da un valor aleatorio.
    return res


#imagen_1 = './Train/rec1-1.jpg'
