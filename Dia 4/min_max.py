#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# detectan valores mas altos y mas bajos en una funcion, 
# sirve tanto para valores num.ericos como alfabéticos

lista = [58, 96, 72, 64, 35]
menor = min(lista)
mayor = max(lista)
print(f'el numero menor es {menor}')
print(f'el numero mayor es {mayor}')

nombres = ['juan', 'pablo', 'alicia', 'carlos']
print(min(nombres))

# Busca primero en minusculas y despues en mayusculas
# para que no se presente este problema, trata siempre de convertir el texto a minusculas
nombre = 'Carlos'
print(min(nombre))

nombre = 'carlos'
print(min(nombre))

dic = {'C1':45, 'C2':11}
# llama por keys
print(min(dic))
# llama por values
print(min(dic.values()))

# Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada 
# valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5] 
valor_maximo = max(lista_numeros)
print(valor_maximo)

# Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo
# en una variable llamada rango:
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
maximo = max(lista_numeros)
minimo = min(lista_numeros)
rango = maximo - minimo
print(rango)

# Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente 
# diccionario:
# Almacena dicho valor en una variable llamada edad_minima.
# También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable 
# llamada ultimo_nombre.
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(f'Edad minima: {edad_minima}')
print(f'Ultimo nombre: {ultimo_nombre}')
