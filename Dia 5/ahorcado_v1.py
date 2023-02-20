#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
from random import choice

# funcion que devuelven
def elegir_palabra(mi_lista):
    palabra_elegída = choice(mi_lista)
    letras_unicas = len(set(palabra_elegída))
    return palabra_elegída, letras_unicas 

def pedir_letra():
    letra_elegida = ''
    es_valido = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valido:
        # El usuario ingresa una letra pero solo cierta letra
        letra_elegida = input('Ingrese una letra para descubrir la palabra secreta: ')
        # debo convertir la letra a minusculas
        letra_elegida = letra_elegida.lower()
        # verifico si la letra pertenece al abecedario y si la longitud de la letra seleccionada es 1
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            #de ser verdadero, asigno True a es_valido
            es_valido = True
        else:
            # no se han cumplido las opciones
            print('No has elegido una letra correcta')
    # retorno la letra elegida
    return letra_elegida
   
def mostrar_nuevo_tablero (palabra_elegida):
    # Saludo
    print('Bienvenido al juego del ahorcado!\n')
    # va a contener la palabra oculta que se va adivinando
    lista_oculta = []
    # hago iterar en cada letra de la palabra
    for letra in palabra_elegida:
        #comparo cada letra con lo que me arroja el método chequear_letra
        if letra in letras_correctas:
            # si está en las letras correctas a lista oculta asigno letra
            lista_oculta.append(letra)
        else:
            # si no está en las letras correctas a lista oculta asigno un gion
            lista_oculta.append('_')
    # imprime el estado de adivinación con un espacio
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    # variable para determinar si el juego se acaba
    fin = False
    # chequeamos si la letra está em la palabra oculta
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        # anexamos a la lista la letra elegida
        letras_correctas.append(letra_elegida)
        # son los aciertos
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print(f'Ya has encontrado la letra {letra_elegida}, intenta con otra letra ')
    else:
        # anexamos a la lista la letra incorrecta 
        letras_incorrectas.append(letra_elegida)
        # cada que desacierto se incrementa en 1
        vidas -= 1
    # verificamos si vidas == 0
    if vidas == 0:
        # a la variable fin, asignamos el predicado del método perder
        fin = perder()
    # verificamos si coincidencias == letras unicas para determinar si ha ganado
    elif coincidencias == letras_unicas:
        # a la variable fin, asignamos el predicado del método ganar
        fin = ganar(palabra_oculta)
    # retornamos vidas, fin y coincidencias
    return vidas, fin, coincidencias

# retorna el predicado y texto que indica que ha perdido
def perder():
    print('Te has quedado sin vidas')
    print(f'La palabra oculta era {palabra}')
    return True
 
# retorna el predicado y el texto que indica que ha ganado 
def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('Felicitaciones, has encontrado la palabra!!!')
    return True

palabras = ['mama', 'agudo', 'enano', 'papa', 'ataxia', 'hijo', 'cocodrilo', 'cirugia', 'matematica']

# almacena las letras correctas
letras_correctas = []
# almacena las letras incorrectas
letras_incorrectas = []
# Cantidad de intentos
intentos = 6
# cantidad de aciertos
aciertos = 0
# validar si el juego termió, inicia en false porque aun no lo ha hecho
juego_terminado = False
# se asigna a las variables palabra y letras_unicas, el resultado de elegir_palabra(palabras)
palabra, letras_unicas = elegir_palabra(palabras)
# se muestra mientras no ha terminado el juego
while not juego_terminado:
    print('\n'+ '*' * 54 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '_'.join(letras_incorrectas))
    print(f'Vidas : {intentos}')
    print('\n'+ '*' * 54 + '\n')
    letra = pedir_letra()
    # se asigna a las 3 variables lo que retorna chequear_letra() que es vidas, fin y coincidencias
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    # al metodo juego terminado, se asigna lo que trae fin
    juego_terminado = terminado
