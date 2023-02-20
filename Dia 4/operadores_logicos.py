#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
mi_bool = 4 < 5 < 6
print(mi_bool)

mi_bool = 4 < 5 > 6
print(mi_bool)

mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool = 4 < 5 == 2 + 3
print(mi_bool)

# and es verdadera cuando ambas proposiciones son verdaderas de lo contrario es falsa 
# y tiene similitud con la multiplicacion True == 1
mi_bool = 55 == 55 and 'perro' == 'perro'
print(mi_bool)

# or es falsa cuando ambas proposiciones son falsas, de lo contrario es verdadera 
# y tiene similitud con la suma False == 0
mi_bool = 1 == 100 or 3 == 3
print(mi_bool)

texto = 'Esta frase es breve'

mi_bool = 'frase' in texto
print(mi_bool)

mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool)

mi_bool = ('frase' in texto) or ('python' in texto)
print(mi_bool)

mi_bool = not 'a' == 'a'
print(mi_bool)

mi_bool = not ('a' != 'a')
print(mi_bool)
