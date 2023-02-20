#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Lista inicial
from random import randint, shuffle
from secrets import choice

palitos = ["-","--","---","----"]

# mezclar palitos
def mezclar(lista_palitos):
    shuffle(lista_palitos)
    return lista_palitos

# pedirle a l usuario que escoja el numero
def probar_suerte():
    intento = ""
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4: ")    
    return int(intento)

# comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == "-":
        print("A lavar los platos")
    else:
        print("Esta Vez te has salvado")    
    print(f"Te ha tocado {lista[intento-1]}")

# se mezclan los palitos
palitos_mezclados = mezclar(palitos)
# se muestran los palitos mezclados podemos hacer trampa
# print(palitos_mezclados)
# eligue una posicion entre el 1 y el 4 para escoger el paliro
seleccion = probar_suerte()
# se envian los palitos mezclado y la posicion del intento
chequear_intento(palitos_mezclados, seleccion)

# Práctica sobre Interacción entre Funciones 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
# Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores 
# aleatorios.
# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta 
# segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de 
# estos valores:
# Si la suma es menor o igual a 6:
# "La suma de tus dados es {suma_dados}. Lamentable"
# Si la suma es mayor a 6 y menor a 10:
# "La suma de tus dados es {suma_dados}. Tienes buenas chances"
# Si la suma es mayor o igual a 10:
# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
# Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.

from random import *
# primera funcion lanzar_dados
def lanzar_dados():
    lista1 = randint(1,7)
    numero1 = str(lista1)
    dado1 = int(choice(numero1))
    lista2 = randint(1,7)
    numero2 = str(lista2)
    dado2 = int(choice(numero2))
    return dado1, dado2

# segunda funcion evaluar_jugada
def evaluar_jugada(dado1_lanzado, dado2_lanzado):
    suma_dados = dado1_lanzado + dado2_lanzado
    if suma_dados <= 6:
        return(f"La suma de tus dados es {suma_dados}. Lamentable.")
    elif suma_dados > 6 and suma_dados < 10:
        return(f"La suma de tus dados es {suma_dados}. Tienes buenas chances.")
    elif suma_dados >= 10:
        return(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora.")

dado1_lanzado, dado2_lanzado = lanzar_dados()
print(dado1_lanzado, dado2_lanzado)
print(evaluar_jugada(dado1_lanzado, dado2_lanzado))

# Práctica sobre Interacción entre Funciones 2
# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros),
# y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y 
# eliminando el valor más alto. El orden de los elementos puede modificarse.

# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función,
# y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

# Funcion 1 reducir_lista(lista_numeros)
def reducir_lista(lista_numeros):
    lista = set(lista_numeros)
    lista = list(lista)
    mas_alto = max(lista)
    indice = lista.index(mas_alto)
    lista.pop(indice)
    return lista

# Funcion 2 promedio()
def promedio(lista_devuelta):
    contador = 0
    media = 0
    for n in lista_devuelta:
        media += n
        contador += 1
    media = media/contador 
    return media

lista_numeros = [1,2,15,7,2]
lista_devuelta = reducir_lista(lista_numeros)
print(promedio(lista_devuelta))

# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función
# debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del 
# lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con 
# valores y llamarla lista_numeros).
# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla 
# (devolverla como lista vacía []).
# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.

from random import *
# Funcion 1 lanzar_moneda()
def lanzar_moneda():
    moneda = ["Cara", "Cruz"]
    eleccion = choice(moneda) 
    return eleccion

# funcion 2 probar_suerte()
def probar_suerte(lanzamiento, lista_numeros):
    for n in lista_numeros:
        if lanzamiento == "Cara":
            print("La lista se autodestruirá")
            lista_numeros.clear()
        elif lanzamiento == "Cruz":
            print("La lista fue salvada")
    return lista_numeros
lanzamiento = lanzar_moneda()
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = probar_suerte(lanzamiento, lista_numeros)
print(resultado)