#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Generar numeros aleatorios por medio de importar métodos en python

from random import *

# randint es algo asi como integer aleatorio
aleatorio = randint(1,50)
print(aleatorio)

# uniform es algo asi como float aleatorio
aleatorio = round(uniform(1,5),1)
print(aleatorio)

# random elige un numero decimal entre o y 1, fraccion de un entero
aleatorio = random()
print(aleatorio)

# choise seleccion aleatoria dentro de los elementos de una lista
colores = ['azul', 'rojo', 'verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

# shafle mezcla aleatoriamente
numeros = list(range(5, 51, 5))
shuffle(numeros)
print(numeros)

# Implementa la función randint() de la librería random que te permita obtener un número entero 
# del 1 al 10, y almacena dicho valor en una variable llamada aleatorio
aleatorio = randint(1,10)
print(aleatorio)
num = str(aleatorio)
num1= choice(num)
print(num1)

# Implementa la función random() de la librería random que te permita obtener un número decimal 
# entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio
aleatorio = random()
print(aleatorio)

# Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de 
# nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)