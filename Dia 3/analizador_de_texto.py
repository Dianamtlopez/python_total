#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""Proyecto Analizador de texto"""

print("Hola, Bienvenido al analizador de textos!\n")
# Captura de datos tipo texto
texto = input("Ingresa el texto deseado! ")
# Convertir Variable a minusculas
texto = texto.lower()

print("\nIngrese 3 letras de su elección, para verificar si la letra existe en el texto ingresado\ny si éstas se repiten:\n")
# Solicitar 3 caracteres o palabras para verificar si existen o no en el texto
# se crea lista para almacenar las letras o palabras que el usuario digite
letras = []
index = 0
while index < 3:
    # Captura de datos tipo texto
    letra = input(f"Ingrese la letra No {index+1}: ")
    # Convertir Variable a minusculas
    letra = letra.lower()
    # Asignar el contenido de letra a la lista letras
    letras.append(letra)
    # Incremento el Contador
    index += 1

# Imprimo las letras o palabras ingresados para la busqueda
print(f"\nLas letras seleccionadas por usted son las siguientes: {letras}")

# primero debo evaluar si los caracteres estan o no en la lista
# Creo la lista n_letra para almacenar las letras existentes en el texto
n_letra = []
# creo la lista eliminar para almacenar las letras no existentes
eliminar = []
cont = 0
# mientras el contador sea menor a la longitud de la lista de letras ingresadas
while cont < len(letras):
    # verifico si cada letra ingresada existe o no en el texto inicial
    if texto.find(letras[cont]) != -1:
        # alimento la lista de letras que si existen en el texto inicial
        n_letra.append(letras[cont])
    else:
        # alimento la lista de letras que no existen en el texto inicial
        eliminar.append(letras[cont])
    cont += 1

# Imprimo las letras no encontradas
print(f"letras no encontradas en el texto son las siguientes: {eliminar}\n")

# creo la variable resultado para mostrar las letras ingresadas y las veces que estas se
# repiten en el texto inicial
resultado = ""
for i in n_letra:
    resultado += (f"La letra {i}, aparece {texto.count(i)} veces.\n")
# imprimo las letras y las veces que estas se repiten en el texto inicial
print(resultado)
    
# se transforma la variable texto a una lista separada por espacios y así podemos 
# determinar cuantas palabras hay en dicha lista por medio de la funcion len()
lista_texto = texto.split()

# muestro la cantidad de palabras que tiene el texto ingresado
print(f"El texto ingresado:\n({texto}).\ncuenta con {len(lista_texto)} palabras\n")

# para saber cual es la primera letra del texto
print(f"La primera letra del texto ingresado es : {texto[0]}")

# para saber cual es el ultimo elemento del texto
print(f"La ultima letra del texto ingresado es: {texto[-1]}\n")

# Para invertir el orden de las palabras en la lista, debemos aplicar la funcion reverse()
lista_texto.reverse()

# Se une cada item de la lista por medio de un espacio y lo asigno a una variable 
n_texto = " ".join(lista_texto)

# muestro el nuevo texto
print(f"{n_texto}\n")

# Evaluamos si la palabra python se encuentra en el texto inicial cuyo resultado es un booleano
resultado = "python" in texto

# Creamos un diccionario para mostrar al usuario si la palabra fue o no encontrada
diccionario = {"True":"La palabra Python ha sido encontrada en el texto.","False":"La palabra Python no ha sido encontrada en el texto."}

if resultado == True:
    print (diccionario["True"])
else:
    print (diccionario["False"])