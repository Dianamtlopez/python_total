#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

# medir el tiempo de ejecucion en el códigp
# time
# timeit
import time

numero = 10000000

def prueba_1(numero):
    lista_1 = []
    for num in range(1, numero+1):
        lista_1.append(num)
    return lista_1
#******************************************************

def prueba_2(numero):
    lista_2 = []
    contador = 1
    while contador <= numero:
        lista_2.append(contador)
        contador += 1
    return lista_2
#******************************************************

def prueba_3(numero):  
    lista_3 = [i for i in range(1, numero+1)]
    return lista_3
#******************************************************

# medir el tiempo de ejecucion en el códigp
# Inicio_1 nos da la hora exacta del inicio de la ejecucion
inicio_1 = time.time()
prueba_1(numero)
# Final_1 nos da la hora exacta del fin de la ejecucion
final_1 = time.time()
# Obtenemos el tiempo exacto de ejecucion
print(final_1-inicio_1)
#******************************************************

# Inicio_1 nos da la hora exacta del inicio de la ejecucion
inicio_2 = time.time()
prueba_2(numero)
# Final_1 nos da la hora exacta del fin de la ejecucion
final_2 = time.time()
# Obtenemos el tiempo exacto de ejecucion
print(final_2-inicio_2)
#******************************************************

# Inicio_1 nos da la hora exacta del inicio de la ejecucion
inicio_3 = time.time()
prueba_3(numero)
# Final_1 nos da la hora exacta del fin de la ejecucion
final_3 = time.time()
# Obtenemos el tiempo exacto de ejecucion
print(final_3-inicio_3)

# Identifica el tiempo de ejecucion de un bloque de codigo especifico
import timeit

declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista
'''
# lo que hace timeit es repetir 100000 veces el código para que el tiempo sea mayor
# y poder obtener un tiempo de ejecución más preciso
duracion = timeit.timeit(declaracion, mi_setup, number = 10000000)
print(f'Ejecución real con for: {duracion}')
# *****************************************************************************

declaracion_2 = '''
prueba_while(10)
'''

mi_setup_2 = '''
def prueba_while(numero):
    lista_2 = []
    contador = 1
    while contador <= numero:
        lista_2.append(contador)
        contador += 1
    return lista_2
'''
# lo que hace timeit es repetir 100000 veces el código para que el tiempo sea mayor
# y poder obtener un tiempo de ejecución más preciso
duracion_2 = timeit.timeit(declaracion_2, mi_setup_2, number = 10000000)
print(f'Ejecución real con while: {duracion_2}')
# *****************************************************************************

declaracion_3 = '''
prueba_comprehension(10)
'''

mi_setup_3 = '''
def prueba_comprehension(numero):  
    lista_3 = [i for i in range(1, numero+1)]
    return lista_3
'''
# lo que hace timeit es repetir 100000 veces el código para que el tiempo sea mayor
# y poder obtener un tiempo de ejecución más preciso
duracion_3 = timeit.timeit(declaracion_3, mi_setup_3, number = 10000000)
print(f'Ejecución real con prueba_comprehension: {duracion_3}')