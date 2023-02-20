#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""Propiedades de los Strings"""

# No permite asignacion de items, por lo tanto son inmutables
# puedo cambiar el contenido de la variable pero no al string como tal
nombre = "Carina"
# nombre[0] = "K"

# Los strings se pueden concatenar
n1 = "Kari"
n2 = "na"
resultado = n1+n2
print(resultado)

# Los strings se pueden multiplicar
resultado1 = resultado * 10
print(resultado1)

# Pueden Contener varias líneas de código
poema = """Mil pequños peces blancos
como si hirviera
el color del agua"""
print(poema)

# Preguntar si un caracter o palabra se encuentra en un string
print("agua" in poema)
print("sol" not in poema)

# Conocer el largo de un string, incluye letras numeros, signos etc
texto = "Hola mundo!"
print(len(texto))