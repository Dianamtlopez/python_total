#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
""" Redondear numeros
    1 si el valor decimal es < 0.5, el resultado es la parte entera
    2 si el valor decimal es >= 0.5, el resultado es la parte entera más 1
"""

# La funcion round con el parametro solo, redondea ese parametro
resultado = round(90/7)
print(resultado)
print(type(resultado))

# La funcion round separado por coma y un segundo parámetro, devuelve la
# cantidad de decimales como valga el segundo parametro 
valor = round(95.666666666,2)
print(valor)
print(type(valor))
