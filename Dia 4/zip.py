#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# combina dos o mas listas entrelazando sus elemetos en una tupla
# zip llega hasta el largo de la lista mas corta, si queremos agregar 
# items, ambas listas deben quedar de igual tamaño.

nombres = ['ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]

combinados = zip(nombres, edades)
combinados = list(combinados)
print(combinados)

ciudades = ['Lima', 'Madrid', 'Mexico']
combinados = zip(nombres, edades, ciudades)
combinados = list(combinados)
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f'{nombre}, tiene {edad} años y vive en {ciudad}.')

# Muestra en pantalla frases como la del siguiente ejemplo:
# La capital de Alemania es Berlín
# Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida 
# y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = zip(paises, capitales)
combinados = list(combinados)

for  pais, capital in combinados:
    print(f'La capital de {pais} es {capital}')

# Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras,
# dentro de la variable mi_zip.

marcas = ['Adidas', 'Nike', 'Kappa', 'Scketcher', 'Lacoste']
productos = ['Guallos', 'Gorras', 'Zapatillas', 'Sudaderas', 'Camisetas']
mi_zip = list(zip(marcas, productos))

# Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés 
# (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable
# numeros:
# uno / um / one
# dos / dois / two
# tres / três / three
# cuatro / quatro / four
# cinco / cinco / five
# El resultado deberá seguir la estructura:

español = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']
mi_zip = zip(español, portugues, ingles)
print(list(mi_zip))