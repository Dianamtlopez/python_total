#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
""" Booleanos
    signos usados con los booleanos
    > mayor que
    < menor que
    >= mayor o igual que
    <= menor o igual que
    == igual que
    != diferente que            
    
    los booleanos son la base de la inteligencia artificial, son los que permiten que los 
    programas tomen decisiones logicas basadas en el cumplimiento o no de condiciones
    valores True o False
"""

# Declaración de forma directa
var1 = True
print(type(var1))
var2 = False
print(type(var2))

# Declaración de forma indirecta
mi_bool = 5 > 4
print(type(mi_bool))
print(mi_bool)

# En algunos códigos nos encontramos
numero = bool(5 < 6)
print(type(numero))
print(numero)

# la siguiente asignacion, SIEMPRE asigna un valor falso
numero = bool()
print(type(numero))
print(numero)

lista = [1,2,3,4,5]
control = 5 in lista
print(type(control))
print(control)

palabra = "exito"
print(palabra[4])
