#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
# Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio.

def devolver_distintos(a,b,c):
    suma = a+b+c
    lista = [a,b,c]
    # Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
    if suma > 15:
        return max(lista)
    # Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
    elif suma < 10:
        return min(lista)
    # Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio
    else:
        lista.sort()
        return lista[1]

resultado = devolver_distintos(5,3,4)
print(resultado)

# Ejercicio 2
# Escribe una función (puedes ponerle cualquier nombre quequieras) que reciba cualquier palabra 
# como parámetro, y quedevuelva todas sus letras únicas (sin repetir) pero en ordenalfabético
# Por ejemplo si al invocar esta función pasamos la palabra"entretenido", 
# debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']

# Libreria para el uso de string.ascii_lowercase, que sirve para traer el abcdario ascci sin la ñ en minuscula
# Usado para expresiones regulares

def parametro_palabra(palabra):
    # se asigna el texto convertido en minuscula a una varible
    texto = palabra.lower()
    # se convierte la cadena en conjunto para quitar caracteres repetidos
    conjunto = set(texto)
    # se convierte el set a lista para su manipulacion
    lista = list(conjunto)
    new_lista = []
    for letra in lista:
        # se compara si el caracter se encuentra en la lista ascci
        if letra in 'abcdefghijklmnñopqrstuvwxyz':
            # se agrega cada caracter a la lista
            new_lista.append(letra)
    # se ordena la lista resultante
    new_lista.sort()
    # se envía la lista
    return new_lista

texto = "Hola Mundo!, como estas?"
resultado = parametro_palabra(texto)
# para poder visualizar el retorno, debo colocar el print
print(f'este es el resultado {resultado}')

# Ejercicio 3
# Escribe una función que requiera una cantidad indefinida deargumentos. 
# Lo que hará esta función es devolver True si en algún momento se ha ingresado al numero cero 
# repetido dosveces consecutivas.

def numeros_cero(*args):
    cont = 0
    for arg in args:
        # Comparamos el indice actual con el siguiente
        if arg == 0 and arg == args[cont + 1]:
            return True # al retornar, se sale del for
        else:
            pass
        # si no ha encontrado ceros, incrementa el contador, para evaluar los indices
        cont += 1
    # Como no ha encontrado dos ceros concecutivos retorna false
    return False

lista = 1,2,3,4,0,0,5,6,0,0
# para visualizar el return debo colocar print
print(numeros_cero(*lista))

# Ejercicio 4
# Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
# Esta función va a mostrar en pantalla cuántos números primos hay en el rango que va 
# desde cero hasta ese número incluido, y va a devolver la cantidad de números primos 
# que encontró Aclaración, por convención el 0 y el 1 no se consideran primos.

def contar_primos(numero):
     # si el usuario ingresa un numero menor a 2
    if numero < 2:
        return 0
    # partimos del hecho que los numeros primos inician en 2
    primo = [2]
    # comenzamos las verificaciones desde el numero 3 contiene chequeando desde el 3 en adelante
    iteracion = 3
    # pasa por cada numero que van desde el 3 hasta el numero elegido
    while iteracion <= numero:
        # Va de dos en dos porque todos los numero pares no son primos excepto el 2, asi hacemos 
        # el programa mas liviano, en este caso iteraria [3,5,7...]
        for n in range(3,iteracion,2):
            # si la iteracion % n == 0, no es primo
            if iteracion % n == 0:
                # por cada numero par se incrementa iteración en 2
                iteracion += 2
                break
        else:
            # En este lugar ya sabemos que no es par, por lo tanto es primo y lo anexamos a la lista
            primo.append(iteracion)
            # para que continue iterando que no se detenga debemos hacer el respectivo incremento
            iteracion += 2
    # imprimimos la lista
    print(primo)
    # retornamos la cantidad de primos encontrados
    return len(primo)
# para visualizar return, debo colocar el print
print(contar_primos(20))