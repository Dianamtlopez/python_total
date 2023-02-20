#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
mi_texto = "Esta es una prueba"

# Mostrar que caracter se encuentra de acuerdo a la posiciòn
resultado = mi_texto[0]
print(resultado)
resultado = mi_texto[9]
print(resultado)
resultado = mi_texto[-4]
print(resultado)

# Para saber en que lugar se encuentra la posicion de un caracter
resultado = mi_texto.index("n")
print(resultado)
print(type(resultado))

# Para saber en que lugar se encuentra la posicion de un caracter en su primera vez que lo encuentra
resultado = mi_texto.index("a")
print(resultado)

# muestra el indice donde inicia la cadena buscada, es sensible a mayusculas y a hortografía
resultado = mi_texto.index("prueba")
print(resultado)

# Para saber en que lugar se encuentra la posicion de un caracter desde la posicion 5 en adelante
resultado = mi_texto.index("a",5)
print(resultado)

# Para saber en que lugar se encuentra la posicion de un caracter desde la posicion 5 en adelante, hasta el numero 11
resultado = mi_texto.index("a", 5, 11)
print(resultado)

# rindez, busca de izquierda a derecha
resultado = mi_texto.rindex("a")
print(resultado)