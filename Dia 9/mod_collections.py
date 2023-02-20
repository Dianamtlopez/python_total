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

frase = "Al pan pan y al vino vino"
print(Counter(frase))
print(Counter(frase.split()))

# Podemos asignar counter a variables
serie = Counter([1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4])
# Más comuún, si envío como parametro un numero, este va a mostrar la cantidad de tuplas que solicito
print(serie.most_common(3))


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