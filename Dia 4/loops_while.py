#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# loops while
monedas = 5
while monedas > 0:
    print(f'Tengo {monedas} monedas.')
    monedas -= 1
else:
    print('No tengo mas dinero.')

# Ejemplo de ciclo while
respuesta = 's'
while respuesta == 's':
    respuesta = input(']Quieres seguir? (s/n): ')
else:
    print('Gracias!s')

# Ejemplo de while con pass Significa pasar, para que yo pueda avanzar
respuesta = 'n'
while respuesta == 's':
    pass 
print('Hola')

# Ejemplo de for con break Significa interrumpir, interrumpe la operacion actual y sale del ciclo
nombre = input('Tu nombre: ')
for letra in nombre:
    if letra == 'a':
        break 
    print(letra)

# Ejemplo de continue, interrumpe operacion actual, pero vuelve al comienzo y continúa
# con la siguiente ejecución
nombre = input('Tu nombre: ')
for letra in nombre:
    if letra == 'a':
        continue 
    print(letra)
