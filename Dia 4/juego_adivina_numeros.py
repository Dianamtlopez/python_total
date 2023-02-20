#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
""" El programa le va a preguntar al usuario su nombre, y luego le va a decir algo así como “Bueno, Juan, 
    he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número”.
    Entonces, en cada intento el jugador dirá un número y el programa puede responder cuatro cosas distintas"""
from random import *

print("ADIVINA ADIVINADOR")

nombre = input('Ingresa tu nombre: ')

print(f"Hola {nombre}, Bienvenid@!")
print("\nInstrucciones del juego:\nHe pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar.\n¿Cuál crees que es el número?")

numero = list(range(1,101))
num_propuesto = choice(numero)

jugada_ini = 0
while jugada_ini <= 8:
    # Insertar un numero para adivinar
    respuesta = int(input(f'Intento {jugada_ini+1} de 8, Ingresa un numero para adivinar el número secreto: '))
    jugada_ini += 1
    
    # Si el número que dijo el usuario es menor a 1 o superior a 100
    # Tambien funcion (if propuesta not in range(1,101))
    if respuesta < 1 or respuesta > 100:
        print(f'{nombre}, has elegido un número que no está permitido.')
    # Si el número que ha elegido el usuario es menor al que ha pensado el programa
    elif respuesta < num_propuesto:
        print(f'{nombre}, Tu respuesta es incorrecta y has elegido un número menor al número secreto.')
    # Si el usuario eligió un número mayor al número secreto
    elif respuesta > num_propuesto:
         print(f'{nombre}, Tu respuesta es incorrecta y has elegido un número mayor al número secreto')
    # Si el usuario acertó el número secreto
    elif respuesta == num_propuesto:
        print(f'{nombre}, Felicitaciones! Has ganado despues de {jugada_ini}, intentos')
        break
    # Si el usuario no ha acertado en este primer intento.
    if jugada_ini == 8:
        print(f'\n{nombre}, Has perdido despues de {jugada_ini} jugadas.')
        print(f'Se han agotado los intentos permitidos!, el numero secreto era el {num_propuesto}.')
        validar = input('Si deseas volver a jugar ingresa S/N: ')
        validar = validar.lower()
        if validar == 's':
            num_propuesto = choice(numero)
            jugada_ini = 0
        else:
            print(f'Has decidido salir!')
            break

print('Hasta la próxima...')

