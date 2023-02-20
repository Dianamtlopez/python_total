#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# rango

# formas anteriores forma ineficiente
lista = [1,2,3,4]

for numero in lista:
    print(numero)

# forma eficiente con range imprime los numeros del 1 al 5
for numero in range(1,6):
    print(numero)

# imprime los numeros del 20 al 30 de 3 en 30
for numero in range(20, 31, 3):
    print(numero)

# crear una lista del 1 hasta el 100
lista = list(range(1,101))
print(lista)

# Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). 
# Almacena dicha lista en la variable mi_lista.
lista = list(range(2500,2586))
print(lista)

# Utilizando la función range(), crea en una única linea de código una lista formada por todos los
# números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
lista = list(range(3, 301, 3))
print(lista)

# Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). 
# Almacena el resultado en una variable llamada suma_cuadrados.
# Para ello:
# Crea un rango de valores que puedas recorrer en un loop
# Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear 
# variables intermedias (de manera opcional).
# Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.
suma_cuadrados = 0
lista = list(range(1,16))
for numero in lista:
    suma_cuadrados += numero**2
print(suma_cuadrados)