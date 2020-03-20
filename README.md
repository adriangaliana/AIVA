# AIVA-Reconocimiento-de-componentes-en-circuitos
El proyecto consiste en que dadas unas imágenes de circuitos integrados se obtengan las localizaciones y la cantidad de condensadores de forma cilíndrica. Estos condensadores son vistos como circunferencias en las imágenes ya que son tomadas desde una vista de planta. Se ha creado un modelo entrenado con una batería de 16 imágenes para Train y 8 imágenes para Test. Dicho modelo es el que se pone a disposición del usuario para que pueda encontrar condesadores dada una imagen de entrada.

## Primeros pasos

Estas instrucciones le darán una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y prueba. Consulte la implementación para obtener notas sobre cómo implementar el proyecto en un sistema en vivo.

### Prerequisitos

Qué cosas necesita para instalar el software y cómo instalarlos:

```
1. Disponer de entorno de Python 3
2. Instalar las siguientes librerías: Numpy, ComputerVision
```

### Instalación

Una serie de ejemplos paso a paso que le indican cómo ejecutar un entorno de desarrollo

#### Cómo poner en marcha el proyecto
```
1. Base a instalar:
  1.1 Entorno: Python 3
  1.2 Bibliotecas: Numpy 1.18.2 , OpenCV-python 4.2.0.32 , tensorflow 2.1.0
  1.3 Usar el comando pip install seguido del nombre de la biblioteca a instalar

2. Para descargarse el programa hay que hacer click en el botón de Clone or Download
3. Podrá realizar una muestra de ejemplo de su funcionamiento descargando la foto image_test.jpg
  
```

## Ejecución de los tests

Para comprobar las funciones ejecute test_circuits.py

## Implementación

Se le pasa una imagen a reconocer al módulo reconocedor_mockup.py y este nos devuelve la posición y el número de los condesadores que encuentre en la misma

## Versioning

Las nuevas versiones del proyecto son publicadas en el GitHub del mismo

## Autores

* **Adrián Galiana** - *Trabajo inicial* - [adriangaliana](https://github.com/adriangaliana)
* **Pedro Miguel Martínez** - *Trabajo inicial* - [pedro-miguel-martinez](https://github.com/pedro-miguel-martinez)

Puede mirar la lista de colaboradores [contributors](https://github.com/adriangaliana/AIVA-Reconocimiento-de-componentes-en-circuitos/contributors) que han participado en este proyecto.

## Agradecimientos

* Agradecemos la idea y el apoyo de nuestro profesor José Vélez y de nuestros compañeros del máster
