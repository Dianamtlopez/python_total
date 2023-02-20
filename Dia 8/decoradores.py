#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""
Todo en python es un objeto, incluso las funciones son objetos, 
esto quiere decir que yo puedo asignar una funcion a una variable
En python, podemos definir funciones dentro de otras funciones
"""


def cambiar_letras(tipo):
    
    # Función dentro de función
    def mayuscula(texto):
        print(texto.upper())


    # Función dentro de función
    def minuscula(texto):
        print(texto.lower())


    # Seleccionamos cual es la operacion que queremos realizar
    if tipo == "my":
        return mayuscula
    elif tipo == "mn":
        return minuscula


operacion = cambiar_letras("my")

operacion("palabra")

"""
Entendido esto, ahora podemos crear los decoradores para decorar cualquier 
funcion quee pasemos y como argumento va a recibir una funcion 
"""

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print('adios')
    return otra_funcion

# Si yo quiero que mis funciones queden decoradas, hago lo siguiente
@decorar_saludo
def mayuscula(texto):
    print(texto.upper())


# Si yo quiero que mis funciones queden decoradas, hago lo siguiente
@decorar_saludo
def minuscula(texto):
        print(texto.lower())


minuscula('Python')
mayuscula('Python')


# ahora si no quiero que siempre estos métodos estén decorados hago lo siguiente:


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print('adios')
    return otra_funcion


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
        print(texto.lower())


mayuscula_decorada = decorar_saludo(mayuscula)


# Si quiero llamar solo a mayusculass
mayuscula("diana")


# Pero si quiero llamar a la mayuscula decorada
mayuscula_decorada("diana")

# De esta manera puedo a

minuscula_decorada = decorar_saludo(minuscula)

minuscula("DIANA")

minuscula_decorada("DIANA")