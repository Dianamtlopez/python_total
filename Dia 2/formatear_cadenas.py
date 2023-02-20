#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""Formateo de Strings"""

# asignacion de valores a las variables
x = 10
y = 5

# manipulacion de strings para concatenar variables numéricas con format
print('Mis numeros son {} y {}'.format(x,y))
print('La suma de {} y {}, es igual a {}'.format(x, y, x+y))

# manipulacion de strings para concatenar variables numéricas con f-string
print(f'Mis numeros son {x} y {y}')
print(f'La suma de {x} y {y}, es igual a {x+y}')

# manipulacion de strings para concatenar variables de diferente tipo
color = 'Rojo'
matricula = 123512
print(f'El auto es {color} y su matrícula es {matricula}')