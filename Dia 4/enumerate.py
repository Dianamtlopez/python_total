#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Enumerate, nos hace la vida más fácil, cuando necesitamos acceder a los indices de cada elemento

lista = ['a', 'b', 'c']
indice = 0
for item in lista:
    print(indice, item)
    indice += 1

# hay una manera mas elegante
lista = ['a', 'b', 'c']
for item in enumerate(lista):
    print(item)

# Imprimimos al indice y luego al item
for indice, item in enumerate(lista):
    print(indice, item)

# Imprimimos al indice y luego al item, en un rango del 50 al 55
for indice, item in enumerate(range(50,56)):
    print(indice, item)

# lista de tuplas
mis_tuples = list(enumerate(lista))
print(mis_tuples)
# para tener acceso a los indices [(0, 'a'), (1, 'b'), (2, 'c')]
print(mis_tuples[0][0])
print(mis_tuples[1][0])
print(mis_tuples[2][0])
# Acceso a los items
print(mis_tuples[0][1])
print(mis_tuples[1][1])
print(mis_tuples[2][1])

# Imprime en pantalla frases como la siguiente:
# '{nombre} se encuentra en el índice {indice}'
# Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante 
# enumerate().
# Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.
# Tip: utiliza loops!

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
mis_tuples = list(enumerate(lista_nombres))

for indice, nombre in mis_tuples:
    print(f'{nombre} se encuentra en el índice: \t{indice}')

# Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante 
# enumerate() los índices de cada caracter del string "Python".
# Llama a la lista obtenida con el nombre de variable lista_indices.

lista = "Python"
lista_indices = list(enumerate(lista))
print(lista_indices)

# Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen 
# con M:
# Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los 
# siguientes elementos:
# Loops
# Condicionales if
# El método enumerate()
# Métodos de strings o indexado

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
lista_nombres = list(enumerate(lista_nombres))
for indice, nombre in lista_nombres:
    if nombre.startswith('M'):
        print(f'{nombre} se encuentra en el índice: \t{indice}')