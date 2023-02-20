#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# se implementa para el manejo de argumentos clave valor
def ejemplo(**kwargs):
    print(type(kwargs))

ejemplo(x = 3, y = 5, z = 2)

# Usados para pasar valores compuestos por clave y valor, y manipular estos valores internamente en la función
def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total
print(suma(x = 3, y = 5, z = 2))

# mezcla de argumentos
# orden de argumentos:
# 1. Variables normales
# 2. *args
# 3. **kwargs

def prueva_argumentos(num1, num2, *args, **kwargs):
    # Se visualizan las dos primeras variables
    print(f'El primer valor es: {num1}')
    print(f'El segundo valor es: {num2}')

    # se visualizan los argumentos *args
    for arg in args:
        print(f'args = {arg}')

    # se visualizan los argumentos **kwargs
    for clave, valor in kwargs.items():
        print(f'kwargs: {clave} = {valor}')
    
    # para que no retorne none    

# Se crea la lista de *args
args = [100, 50, 400 , 300]
# Se crea el diccionario de **kwargs
kwargs = {'x': '1', 'y': '2', 'z': '3'}
# Se instancia el objeto
prueva_argumentos(15, 50, *args, **kwargs )
# no tiene return, no hay que imprimir

# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva
# esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    cont = 0
    for clave, valor in kwargs.items():
        cont += 1
    return cont

# Se crea el diccionario de **kwargs
kwargs = {'x': '1', 'y': '2', 'z': '3'}
# Se instancia el objeto
resultado = cantidad_atributos(**kwargs )
# Se muestra el resultado
print(f'La cantidad de atributos es: {resultado}')

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos 
# entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad 
# de argumentos de este tipo.

def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista

# Se crea el diccionario de **kwargs
kwargs = {'x': '1', 'y': '2', 'z': '3'}
# Se instancia el objeto
resultado = lista_atributos(**kwargs )
# Se muestra el resultado
print(f'La lista de valores es: {resultado}')

# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad 
# indetermida de argumentos. Esta función deberá mostrar en pantalla:

# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:
# describir_persona("María", color_ojos="azules", color_pelo="rubio")
# Mostrará en pantalla:
# Características de María:
# color_ojos: azules
# color_pelo: rubio

def describir_persona(nombre, **kwargs):
    print(f'Caracteristicas de {nombre}:')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

nombre = 'Diana'
# Se crea el diccionario de **kwargs
kwargs = {'color_ojos': "Café", 'color_pelo': "Rojo", 'altura': 1.55, 'edad': 41}
# Se instancia el objeto
describir_persona(nombre, **kwargs)