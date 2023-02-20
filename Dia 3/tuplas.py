#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
""" Tuplas,
    son inmutables
    ocupan menos espacio en memoria
    solo para almacenar estructuras que no deseamos que se modifiquen
"""

mi_tuple = (1,2,3,4)
print(mi_tuple)
print(type(mi_tuple))

# imprimir elementos de la tupla, funciona igual que los strings
print(mi_tuple[0])
print(mi_tuple[-1])

# puedo anidar y verificar una tupla dentro de la tupa
mi_tuple1 = (1, 2, (10, 20), 4)
print(mi_tuple1[2][0])

# puedo hacer casting para poderlo modificar
mi_tuple1 = list(mi_tuple1)
print(mi_tuple1)
print(type(mi_tuple1))

mi_tuple1 = tuple(mi_tuple1)
print(mi_tuple1)
print(type(mi_tuple1))

# asignar el contenido de un tuple a diferentes variables
# esto sucede porque al tener la misma cantidad de variables y de valores, automáticamente se asigna
# esto tambien funciona con listas y diccionarios, la condicion es que siempre haya la misma cantidad 
# de variables y elementos
t = (1,2,3)
x,y,z = t
print(x,y,z)

# ver cantidad de elemetos
print(len(t))

# las tuplas tienen solamente 2 mètodos index y count, count nos retorna cuantas vece se repite un elemento 
# en la tupla o apariciones, esto tambien se puede hacer con las listas
t = (1,2,3,2,1,3,4,4,5,6)
print(t.count(1))

# para saber cual es el indice de un valor, esto tambien se puede hacer con las listas
print(t.index(3))