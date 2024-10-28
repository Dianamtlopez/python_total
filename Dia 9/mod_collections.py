#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
from collections import Counter, defaultdict, namedtuple

# Tenemos una serie de numeros que se repiten aleatoriamente, y si aplico el objeto counter
# me va a generar un diccionario cuya clave es el numero y el valor es la cantidad de veces 
# que este numero se repite
numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]
print(Counter(numeros))

frase = "al pan pan y al vino vino"
# En este caso nos cuenta los caracteres de la cadena deseada
print(Counter(frase))
# En este caso cuenta las palabras encontadas 
print(Counter(frase.split()))

# Podemos asignar counter a variables
serie = Counter([1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4])
# Más común, si envío como parametro un numero, este va a mostrar 
# los números según el valor enviado que se repite más veces
print(serie.most_common(3))
# imprimir elementos únicos de la lista
print(list(serie))

# veamos que ocurre en un diccionario normal
mi_dic = {'uno': 'verde',
          'dos': 'azul',
          'tres': 'rojo'}
# cuando ingreso claves que no existen, me sale error 
print(mi_dic['uno'])

# Si creo el diccionario con defaultdict(), le estoy diciendo que cuando se llame un valor que no existe,
# Imprima nada
mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['cuatro'])
print(mi_dic['uno'])

# cuando hago el llamado al diccionario, me va a sacar los valores existentes mas el valor nada
print(mi_dic)

# Tupla nominada o tupla con nombre
mi_tupla = (500, 18, 65)
print(mi_tupla[1])

# Acceder al índice con un nombre
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

# Ahora para llamar a esta persona, imprimo lo siguiente:
print(ariel.altura)
# Ahora, si quiero acceder a la tupla por el indice, tambien puedo hacerlo
print(ariel[2])

# *********************************************************************************
# Práctica Módulo Collections 1
# Aplica un Counter (contador) sobre la lista de números entregada a continuación,
# y almacénalo en una variable llamada contador
from collections import Counter
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)
print(contador)
# *********************************************************************************

# *********************************************************************************
# Práctica Módulo Collections 2
# Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una 
# palabra clave buscada, se cargue con el string "Valor no hallado".
# Carga el diccionario, al menos, con el siguiente par de datos:
# palabra clave = edad
# valor = 44
# Utiliza el método defaultdict del módulo Collections.

mi_diccionario = {'nombre': 'Diana',
          'edad': '43',
          'altura': '1,55'}
print(mi_diccionario['edad'])

# Si creo el diccionario con defaultdict(), le estoy diciendo que cuando se llame un valor que no 
# existe, imprima "Valor no hallado"
mi_diccionario = defaultdict(lambda: 'Valor no hallado')
print(mi_diccionario['peso'])
# *********************************************************************************

# *********************************************************************************
# Práctica Módulo Collections 3
# Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura 
# de datos lineal que permite insertar y eliminar elementos por ambos extremos.
# Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa 
# una deque a partir del módulo collections. Los elementos iniciales de la lista se brindan a 
# continuación.
# ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
# La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el 
# nombre lista_ciudades.

import collections
lista_ciudades = collections.deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

print(lista_ciudades)

print('Deque: ', lista_ciudades)
print('Length: "Tamaño"', len(lista_ciudades))
print('Left end: "Inicio"', lista_ciudades[0])
print('Right end: "Final"', lista_ciudades[-1])

# Agregar valores al inicio
lista_ciudades.appendleft('Bogotá')
print('extendleft: ', lista_ciudades)

# Agregar valores al final
lista_ciudades.append('Santander')
print('extend: ', lista_ciudades)