#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""Fragmentador de palabras"""

texto = "ADCDEFGHIJKLM"

# Caracter en el cual inicia la fragmentacion
fragmento = texto[2]
print(fragmento)

# Caracter en el cual inicia y hasta el valor que ingresamos para terminar la fragmentacion sin incluir el valor final
fragmento = texto[2:5]
print(fragmento)

# Caracter en el cual inicia y hasta el final
fragmento = texto[2:]
print(fragmento)

# Caracteres desde el inicio y hasta el 5 sin incluirlo
fragmento = texto[:5]
print(fragmento)

# Caracter en el cual inicia y hasta el valor que ingresamos para terminar la fragmentacion sin incluir 
# el valor final y cada cuantos caracteres se va a mostrar
fragmento = texto[2:10:2]
print(fragmento)

# desde el cero hasta el último indice de 2 en 2
fragmento = texto[::2]
print(fragmento)

# Obtiene toda la cadena al reves
fragmento = texto[::-1]
print(fragmento)

# Obtiene la cadena al reves de 2 en 2
fragmento = texto[::-2]
print(fragmento)

frase = "Controlar la complejidad es la esencia de la programación"
resultado = frase[10:13]
print(resultado)