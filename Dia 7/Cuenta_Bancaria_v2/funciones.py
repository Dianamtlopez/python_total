#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* NUEVO PLANTEAMIENTO: * JOSÉ LUIS CUENCA LAGUNA     *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
import platform
from os import system

from clases import Cliente


def limpia_pantalla():
    sistema = platform.system()
    if sistema == 'Linux':
        system('clear')
    else:
        system('cls')


def encabezado(cliente):
    print(
        "*****************************************************************\n")
    print(cliente)
    print(
        "\n*****************************************************************\n"
    )


def menu():
    eleccion_menu = ''
    # verificamos que el ingreso sea un numero por mas que esté en un string
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(
            1, 5):
        limpia_pantalla()
        print('Elige una opción: ')
        print("""
        [1] - Depositar Dinero
        [2] - Retirar Dinero
        [3] - Consultar Saldo
        [4] - Salir del programa
        """)
        eleccion_menu = input()
    return eleccion_menu


def crear_cliente():
    limpia_pantalla()
    nombre = input("Digite su nombre: \t")
    nombre = nombre.upper()
    apellido = input("Digite sus apellidos: \t")
    apellido = apellido.upper()
    num_cuenta = ''
    while not num_cuenta.isnumeric() or len(num_cuenta) != 4:
        num_cuenta = input("Digite los ultimos 4 digitos de su cuenta: ")
    cliente = Cliente(nombre, apellido, num_cuenta)
    return cliente