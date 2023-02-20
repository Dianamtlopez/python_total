#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
x = 6
y = 2
z = 7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

# división al piso elimina decimales y nos da la parte entera
print(f"{z} dividido al piso de {y} es igual a {z//y}")
print(f"{874} dividido al piso de {27} es igual a {874//27}")

# el modulo es cuando se hace una division y quedan valores por operar en divisiones inexactas
# básicamente el modulo es usado cuando queremos saber si un numero es par con el resultado en cero
print(f"{z} modulo de {y} es igual a {z%y}")

# potencia
print(f"{x} elevado a la {y} es igual a {x**y}")

# raiz 
print(f"{x} raiz {y} es igual a {x**(1/y)}")