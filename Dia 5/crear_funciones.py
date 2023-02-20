#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# las funciones permiten crear bloques de código que pueden ser facilmente ejecutados muchas veces y en 
# distintos contextos sin necesidad de repetir el código
# por convención los nombres de las funciones van así mi_funcion
def mi_funcion(nombre):
    """
        Esta funcion se encarga de imprimir un saludo en pantalla
    """
    print(f"Hola {nombre}")
mi_funcion("Willy")

def saludar_personas(nombre):
    """
        Esta funcion sirve para saludar personas
    """
    print(f"Hola {nombre}")
mi_funcion("Willy")

# Práctica Crear Funciones 1
# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"
# Solo debes definir la función, no debes invocarla luego.

def saludar():
    print('Hola Mundo')

# Práctica Crear Funciones 2
# Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada 
# vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.
# Solo debes definir la función y crear la variable, no debes invocar la función luego.

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
nombre = 'Diana'
# se debe retornar para que no devuelva None

# Práctica Crear Funciones 3
# Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea 
# llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
#El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número 
# cualquiera.
# Solo debes definir la función y crear la variable, no debes invocar la función luego.

def cuadrado(un_numero):
    un_numero = un_numero ** 2
    print(un_numero)
un_numero = 50

# Otros ejemplos
def cuadrado(un_numero):
    new_num = []
    new_num = [x**2 for x in un_numero]
    return new_num
un_numero = [1, 2, 3, 4, 5]
resultado = cuadrado(un_numero)
print(resultado)

def cuadrado(un_numero):
    return un_numero ** 2
un_numero = 50
resultado = cuadrado(un_numero)
print(resultado)