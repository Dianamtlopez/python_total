#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# sintaxis:
def mi_funcion(nombre):
    print('Hola ' + nombre)
print(mi_funcion('Diana'))

# En realidad lo que se busca es que la función devuelva algo.
def mi_funcion(nombre):
    return('Hola ' + nombre)
print(mi_funcion('Diana'))

def sumar(num1, num2):
    return num1 + num2
# normalmente lo que hacemos con las funciones es almacenarlas en una variable para usar luego su resultado
resultado = sumar(10,20)
print(resultado)

def multiplicar(num1, num2):
    return num1 * num2
resultado = multiplicar(10,20)
print(resultado)

# Práctica Return 1
# Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número 
# que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:

def potencia(num1, num2):
    return num1 ** num2
resultado = potencia(10,20)
print(resultado)

# Práctica Return 2
# Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares 
# estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, 
# tomaremos la conversión 1 USD = 0.90 EUR.

# Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función 
# y evaluar su resultado.

# Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 
# 0.90 para obtener el monto equivalente en euros.

def usd_a_eur(dolares):
    return dolares * 1.02
dolares = 10
print(usd_a_eur(dolares))

# Práctica Return 3
# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta
# el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

#Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

#También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle
# como argumento a la función creada.

# Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.

def invertir_palabra(palabra):
    # Convierto a mayusculas
    palabra = palabra.upper()
    # tansformo a lista para aplicar funciones de lista
    palabra = list(palabra)
    # transpongo los items
    palabra.reverse()
    # uno en un string
    palabra = "".join(palabra)
    # retorno el string
    return palabra
palabra = "Curso de Python"
print(invertir_palabra(palabra))

# otra manera
def invertir_palabra(palabra):
    # se escribe la palabra de atras para adelante
    palabra = palabra[::-1]
    # se convierte en mayusculas
    palabra = palabra.upper()
    # se retorna la palabra
    return palabra

palabra = "Curso de Python"
print(invertir_palabra(palabra))
