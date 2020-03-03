import unittest
import numpy as np
from reconocedor_mockup import reconocer_imagen, contar_condensadores, posicionar_condensadores

class Test_mockup (unittest.TestCase):
    def test_reconocer (self):
        # Creamos una imagen de prueba
        # matriz = [[1,2,3],[4,5,6],[7,8,9]]
        # im = np.array(matriz, dtype=np.uint8)
        
        """
        
        Este primer test es el que comprueba si pasándole cualquier tipo de imagen se devuelve 
        un TRUE cuando hay condensadores en la imagen de un circuito integrado y FALSE en caso
        contrario.
        
        """
           
        im = './Train/rec1-1.jpg' # imagen ejemplo
        res = reconocer_imagen(im)
        print(res)
        self.assertTrue(('SÍ' in res) == True)

    def test_contar (self):
        # Creamos una imagen de prueba
        # matriz = [[1,2,3],[4,5,6],[7,8,9]]
        # im = np.array(matriz, dtype=np.uint8)
                
        """
        
        Este segundo test es el que comprueba que al pasarle una imagen se devuelve 
        un TRUE cuando hay condensadores y el número que devuelve la función del módulo
        principal es un entero; y FALSE en caso contrario.
        
        """
           
        im = './Train/rec1-1.jpg'
        res = contar_condensadores(im)
        print(type(res))
        self.assertTrue((type(res) is int) == True)


    def test_contar (self):
        # Creamos una imagen de prueba
        # matriz = [[1,2,3],[4,5,6],[7,8,9]]
        # im = np.array(matriz, dtype=np.uint8)
        
        """
        
        Finalmente, el tercer test es el que comprueba que al pasarle una imagen se devuelve 
        un TRUE cuando hay condensadores y se obtiene un número entero en las dos posiciones del res
        que devuelve la función del módulo principal, las cuales marcan la posición del centro radial
        del condensador encontrado; y FALSE en caso contrario.
        
        """
        
        im = './Train/rec1-1.jpg'
        res = contar_condensadores(im)
        print(type(res))
        self.assertTrue((type(res) is int) == True)

    def test_contar (self):
        # Creamos una imagen de prueba
        # matriz = [[1,2,3],[4,5,6],[7,8,9]]
        # im = np.array(matriz, dtype=np.uint8)
        im = './Train/rec1-1.jpg'
        res = posicionar_condensadores(im)
        print(res)
        self.assertTrue((type(res[0]) is int) & (type(res[1]) is int) == True)


if __name__ == '__main__':
    unittest.main()

