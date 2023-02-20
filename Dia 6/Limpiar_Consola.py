#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
from os import system

nombre = input('dime tu nombre: ')
edad = input('dime tu edad: ')

# Limpia pantalla
system('cls')

print(f'Tu nombre es {nombre} y tienes {edad} años')
