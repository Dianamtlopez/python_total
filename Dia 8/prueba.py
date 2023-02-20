#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""
Esta implementacion evalúa y devuelve el código que esperamos   
"""
import unittest
import cambia_texto

class Probar_Cambia_texto(unittest.TestCase):

    def test_mayusculas(self):
        """
        Importante, las funciones de pruebas deben iniciar con la palabra 
        test para que entiendan que deben hacer la respectiva prueba
        """
        # Palabra a comprobar
        palabra = "buen día"
        # Muestra como ueda la palabra si se aploca todo en mayusculas en cambia_texto
        resultado = cambia_texto.todo_mayusculas(palabra)
        # Se llama a self.assertEqual(), es un método de case que shequea dos argumentos, 
        # el resultado y por otro lado coloco, como creería que va a ser el resultado
        self.assertEqual(resultado, 'BUEN DÍA')

    
    # La mayoría de los lenguajes de programación, tienen una clase llamada main que quiere 
    # decir principal, para que el sistema sepa cuando ejecute el programa debe comenzar por 
    # esa clase, python no funciona así, por tal razon esta es una manera de decirle al sistema 
    # cual funcion debe ejecutar y cual no, es una forma de proteger el código 
    if __name__ == '__main__':
        unittest.main()