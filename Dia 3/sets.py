#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
""" Sets
    python reconoce set de esta manera set(1,2,3,4,5,6) o {1,2,3,4,5,6}

    si los datos se ingresaron set(1,2,3,4,5,6), los datos que se anexen 
    solo pueden ir en un conjunto de llaves, parentesis, llaves curvas
    pero deben estr encerrado para que pyton lo lea como un solo elemento

    si el set se creo asi  {1,2,3,4,5,6}, los datos que se anexen los elementos 
    se pueden colocar directamente

    solo admiten elementos únicos, su se agregan elementos repetidos, no hace nada

    los elementos no estan ordenados en indices

    los elementos son inmutables, no puede tener ni listas ni diccionarios
"""

mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

# No se repiten
mi_set = set([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6,7])
print(mi_set)

# set admite tuples porque los datos son inmutable
mi_set = set([1,2,3,4,(1,2,3),6,7])
print(mi_set)

# conocer el largo
print(len(mi_set))

# encontrar un dato en el set
print(2 in mi_set)

# union de set
s1 = {1,2,3}
s2 = {3,4,5,6}
s3 = s1.union(s2)
print(s3)

# agregar datos
s1.add(4)
print(s1)

# eliminar un elemento del conjunto
s1.remove(4)
print(s1)

# descartar elementos y no es lo mismo que eliminar, solo es para evitar errores
s1.discard(1)
print(s1)

# pop elimina un elemento aleatorio ya que los sets no tienen indices
sorteo = s1.pop()
print(sorteo) 

# vaciar el set
s1.clear()
print(s1)