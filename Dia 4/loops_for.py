#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Cuando queremos que un bloque de código se ejecute varias veces

# cantidad definida de iteraciones
nombres = ['Juan', 'Ana', 'Carlos', 'Belén', 'Fran']
saludo = ''
for nombre in nombres:
    print(f'Hola {nombre}!')

lista = ['a', 'b', 'c', 'd']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

lista = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']
# imprime en pantalla los nombres que inician con L
for nombre in lista:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print(f'Nombre {nombre}, no comienza con L')

numeros = [1,2,3,4,5,6]
mi_valor = 0
for numero in numeros:
    mi_valor += numero

print(mi_valor)

# los strings son iterables
palabra = 'python'
for letra in palabra:
    print(letra)

for letra in [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]:
    print(letra)

for a,b,c,d in [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]:
    print(a,b,c,d)
    
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic.keys():
    print(item)
for item in dic.values():
    print(item)
for item in dic.items():
    print(item)
for a,b in dic.items():
    print(a,b)