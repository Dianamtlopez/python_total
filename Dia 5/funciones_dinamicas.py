#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
from unittest import result

def chequear_3_cifras(numero):
    return numero in range(100, 1000)
resultado = chequear_3_cifras(658)
print(resultado)

def chequear_3_cifras(lista):
    comprobar = [n for n in lista if n in range(100,1000)]
    return comprobar
lista = [50, 100, 800, 2000]
resultado = chequear_3_cifras(lista)
print(resultado)

# Devuelve un predicado
def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            # el return cuando encuentra la condicion, corta el loop y devuelve el resultado
            return True
        else:
            pass
    return False
lista = [50, 500, 2000]
resultado = chequear_3_cifras(lista)
print(resultado)

# Devuelve la lista con los valores que cumplen
def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
lista = [50, 500, 2000]
resultado = chequear_3_cifras(lista)
print(resultado)

# Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True 
# si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea 
# una lista llamada lista_numeros con valores positivos y negativos.

# No invoques la función, solo es necesario definirla.

def todos_positivos(lista_numeros):
    for n in lista:
        if n >= 0:
            pass
        else:
            # Devuelve false cuando almenos uno es negativo
            return False
    # Devuelve true cuando todos los valores son positivos
    return True

lista_numeros = [0,1,-1,2,3,-5,4]
resultado = todos_positivos(lista)
print(resultado)

# Práctica Funciones Dinámicas 2
# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) 
# siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
def suma_menores(lista_numeros):
    suma = 0 
    for n in lista_numeros:
        if n in range(0,1000):
            suma += n   
    return suma
lista_numeros = [10,20,500,800,1500,2000]
resultado = suma_menores(lista_numeros)
print(resultado)

# Práctica Funciones Dinámicas 3
# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista 
# (lista_numeros), y devuelva el resultado de dicha cuenta.
def cantidad_pares(lista_numeros):
    contador = 0
    for n in lista_numeros:
        if n % 2 == 0:
            contador += 1
    return contador
# el cero es un numero neutro
lista_numeros = [-3,-2,-5,0,1,2,3]
resultado = cantidad_pares(lista_numeros)
print(resultado)