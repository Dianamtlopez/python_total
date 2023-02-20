#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
""" métodos para cadenas:
    upper()     pasar a mayusculas
    lower()     pasar a minusculas
    split()     separado en partes (lista)
    join()      unir items usando separador
    find()      encontrat un sub-strin
    replace()   reemplazar un sub string
"""

texto = "Este es el texto de Federico"
resultado = texto
print(resultado)

# pasar a mayusculas
resultado = texto.upper()
print(resultado)

# pasar a minusculas
resultado = texto.lower()
print(resultado)

# separado en partes (lista) tomando como separador espacios vacíos
resultado = texto.split()
print(resultado)

# separado en partes (lista) tomando como separador, el parámetro que ingresemos en los parentesis
resultado = texto.split("t")
print(resultado)

# unir items usando separador
a = "aprender"
b = "Python"
c = "es"
d = "genial"

# une las variables en una lista, separandolas por el parametro que yo seleccione en las comillas
e = " ".join([a,b,c,d])
print(e)

# find busca un caracter o in palabra dentro del string, la unica diferencia de index es que cuando 
# no encuentra un caracter, devuelve -1
resultado = texto.find("t")
print(resultado)

resultado = texto.find("texto")
print(resultado)

# el método reemplazar, sirve para tomar un fragmento del texto y reemplazarlo por otro, necesita 2
# parámetros el primero es el texto que quiero eliminar y el segundo es el texto que deseo agregar
resultado = texto.replace("Federico", "Todos")
print(resultado)

resultado = texto.replace("e", "x")
print(resultado)

# une los elementos de la lista y los separa por espacios
lista_palabras = ["La","legibilidad","cuenta."]
resultado = " ".join(lista_palabras)
print(resultado)

# reemplaza palabras en un texto
texto = "Si la implementación es difícil de explicar, puede que sea una mala idea"
resultado = texto.replace("difícil","fácil")
resultado = resultado.replace("mala","buena")
print(resultado)