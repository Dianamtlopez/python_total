#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
from os import system
from package import numeros

p = numeros.perfumeria()
f = numeros.farmacia()
c = numeros.cosmeticos()


def menu():
    
    eleccion_menu = ''
    # verificamos que el ingreso sea un numero por mas que esté en un string
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range (1,5):
        
        system('cls')
        print("******************************************")
        print('* Bienvenido a la farmacia Salud y Vida! *')
        print("******************************************\n")
        print('Elige una opción: ')
        print("""
        [1] - Perfumería
        [2] - Farmacia
        [3] - Cosméticos
        [4] - Salir del programa
        """)
        eleccion_menu = input()
        
    return eleccion_menu


def crear_turno():
    cont = ""
    while cont != 's':     
        eleccion_menu = menu()
        system('cls')
        match eleccion_menu:
            case '1':
                turno = next(p)
            case '2':
                turno = next(f)
            case '3':
                turno = next(c)
            case '4':
                print("Usted ha salido del sistema...")
                quit()
        inf_completa = numeros.decorar_turno(numeros.turno_seleccionado)
        inf_completa(turno)

        input("Presione Enter para continuar...")

crear_turno()

