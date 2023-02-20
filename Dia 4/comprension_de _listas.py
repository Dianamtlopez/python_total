#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
from ast import comprehension

palabra = 'python'
lista = []

# ciclo normal
for letra in palabra:
    lista.append(letra)
print(lista)

#comprehension
lista = [letra for letra in palabra]
print(lista)

# imprime los numeros del 0 al 20 de 2 en dos
lista = [n for n in range(0,21,2)]
print(lista)

# imprime los numeros del 0 al 20 de 2 en dos, divididos por 2 
lista = [n/2 for n in range(0,21,2)]
print(lista)

# muestra todos los numeros que van del 0 al 20 que en la operacion el numero multiplicado * 2 sean mayores que 10
lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista)

# con else # muestra todos los numeros que van del 0 al 20 que en la operacion el numero multiplicado * 2
# sean mayores que 10 y los que sean menores, escriba no
lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista)

# tenemos una lista en pies y queremos pasarla a metros
pies = [10,20,30,40,50]
metros = [n * 3.281 for n in pies]
print(metros)

# Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación
# el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los 
# conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy 
# útiles en tu práctica profesional!
# Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n ** 2 for n in valores]
print(valores_cuadrado)

# Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación
# el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los 
# conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy 
# útiles en tu práctica profesional!
# Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n %2 == 0]
print(valores_pares)

# para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación
# el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los 
# conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte 
# muy útiles en tu práctica profesional!

# Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva
# lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:

# grados_c = (gradosF - 32) * (5/9)

# o expresado de otro modo:

# (grados_f-32) * (5/9)

# La lista de temperaturas es la siguiente:

temperatura_fahrenheit = [32, 212, 275] 
grados_celsius = [(gf-32)*(5/9) for gf in temperatura_fahrenheit]
print(grados_celsius)