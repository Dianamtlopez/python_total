#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Funciones con argumentos definidos
def suma (a,b):
    return a + b
print(suma(5,6))

# Funciones con varios argumentos
def suma_args (*args):
    total = 0
    for arg in args:
       total += arg
    return total
 
print(suma_args(5,6,7,8,9))

# Funciones con varios argumentos
def suma_args (*args):
    return sum(args)

print(suma_args(5,6,7,8,9,500,800))

# Práctica sobre Argumentos Indefinidos (*args) 1
# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, 
# y que retorne la suma de sus valores al cuadrado.
# Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2
    return suma
print(suma_cuadrados(1,2,3))

# Práctica sobre Argumentos Indefinidos (*args) 2
# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, 
# y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo 
# que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*args):
    suma = 0
    valor_absoluto = 0
    for arg in args:
        valor_absoluto = abs(arg)
        suma += valor_absoluto
    return suma
print(suma_absolutos(1,2,3,-2))

# Práctica sobre Argumentos Indefinidos (*args) 3
# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, 
# una cantidad indefinida de números.
# La función debe devolver el siguiente mensaje:
# "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre, *args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg
    return(f'{nombre}, la suma de tus números es {suma_numeros}')

print(numeros_persona("Diana",1,2,3,-2,10,20))
