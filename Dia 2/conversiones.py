#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""Conversiones de variables"""

# Dato Integer
num1 = 20
print(num1)
print(type(num1))

# Dato Float
num2 = 30.5
print(num2)
print(type(num2))

# Conversion implicita ya que python lo hace por si solo
print(num1 + num2)
print(type(num1 + num2))

# Convercion explisita cuando lo hacemos nosotros
num3 = int(num2)
print(num3)
print(type(num3))

# El dato capturado por input es un string, hay que convertirlo al tipo de dato deseado
edad = input('Dime tu edad: ')
edad = int(edad)
print(edad)

# manejo de cadenas y diferentes tipos de variables
nueva_edad = 1 + edad
print('Tu nueva edad es:',nueva_edad)