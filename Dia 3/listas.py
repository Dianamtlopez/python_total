#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""Propiedades de las listas, todo lo de strings, aplica a listas"""

mi_lista = ["a","b","c"]
print(type(mi_lista))

# Tamaño de la lista
resultado = len(mi_lista)
print(resultado)

# Extraer el elemento de la posicion 0
resultado = mi_lista[0]
print(resultado)

# Concatenar listas
mi_lista2 = ["d","e","f","g"]
resultado = mi_lista + mi_lista2
print(resultado)

otra_lista = ["Hola",55,6.1,True]
print(type(otra_lista))

# Las lista sí alteran sus elementos
mi_lista3 = ["a","b","c","d","e","f","g"]
mi_lista3[0] = "alfa"
print(mi_lista3)

# Agregar elementos a las listas
mi_lista3.append("h")
print(mi_lista3)

# Eliminar elementos, cuando pop se coloca 
# sin parametros, interpreta que se quiere eliminar el ultimo de sus elementos
mi_lista3.pop()
print(mi_lista3)

# Eliminar el indice 0
eliminado = mi_lista3.pop(0)
print(mi_lista3)
# ver el elemento borrado
print(eliminado)

# ordenar listas, sort no devuelve nada, por lo tanto no se puede asignar su resultado a una variable
# es importante quedar con el concepto de que la ordena y queda ordenada, cuando se hace el llamado de
# la lista, en adelante, va a estar ordenada
lista = ["g","a","h","k","b"]
print(lista)
lista.sort()
print(lista)

# Para voltear la lista alreves usamos reverse y funciona igual que sort
lista.reverse()
print(lista)


