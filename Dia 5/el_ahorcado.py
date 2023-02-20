#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
from random import choice
from warnings import catch_warnings

# funcion que devuelven lista de palabras a elegir
def elegir_palabra(lista_palabras):
    palabra_elegída = choice(lista_palabras)
    # saber cuantas letras unicas tiene la palabra para luego controlar con aciertos y saber si ha ganado
    letras_unicas = len(set(palabra_elegída))
    # retornamos palabra_elegída y cantidad letras_unicas
    return palabra_elegída, letras_unicas

def pedir_letra():
    # letra elegida por el usuario
    letra_elegida = ''
    # Aun no es valida o no, se inicia en false
    es_valida = False
    # creamos el abecedario
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    # no va a poder salir de bucle, hasta que ponga una letra válida
    while not es_valida:
        # El usuario ingresa una letra pero solo cierta letra
        letra_elegida = input('Ingrese una letra para descubrir la palabra secreta: ')
        # la pasamos a minusculas
        letra_elegida = letra_elegida.lower()
        # si la letra está en el abecedario y su largo es 1
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            # pasamos la variable es_valida a True ya que se cumplen las dos opciones
            es_valida = True
        else:
            # no se han cumplido las opciones
            print('No has elegido una letra correcta')
    # retornamos la letra elegida
    return letra_elegida
   
def mostrar_nuevo_tablero (palabra_elegida):
    # va a contener la palabra oculta que se va adivinando
    lista_oculta = []
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('_')
    # imprime el estado de adivinación
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

def perder():
    print('Te has quedado sin vidas')
    print(f'La palabra oculta era {palabra}')
    return True
    
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

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n'+ '*' * 54 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '_'.join(letras_incorrectas))
    print(f'Vidas : {intentos}')
    print('\n'+ '*' * 54 + '\n')
    letra = pedir_letra()
    
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado