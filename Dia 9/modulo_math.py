#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

import math

# Redondear hacia abajo o el piso
resultado = math.floor(89.665)
print(resultado)  # Salida: 89

# Redondear hacia arriba o el techo
resultado = math.ceil(89.665)
print(resultado)  # Salida: 90

# *********************************************************
# Práctica Módulo Math 1
# Obtén el logaritmo base 10 del número 25, y almacena el resultado en la variable resultado.
# Puedes utilizar el método math.log10()
# Puedes consultar el enlace anterior si quieres conocer más acerca del logaritmo decimal.

resultado = math.log10(25)

# ********************************************************************************************
# Práctica Módulo Math 2
# Obten la raíz cuadrada de pi con la constante math.pi y el método math.sqrt() . Almacena 
# el resultado obtenido en la variable resultado.

resultado = math.sqrt(math.pi)
print(resultado)

# **********************************************************************
# Práctica Módulo Math 3
# Encuentra el factorial de 7 y almacena el resultado en la variable resultado.
# El método a utilizar es factorial()

# Factorial de 7
resultado = math.factorial(7)
print(resultado)  

# si quiero escribir la función, ésta quedaría asi:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Factorial de 7
resultado = factorial(7)
print(resultado)  # También imprime 5040