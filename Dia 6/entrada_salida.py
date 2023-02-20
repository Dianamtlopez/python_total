#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Apertura del archivo
mi_archivo = open("prueba.txt")
# Leer y mostrar todo el archivo
#print(mi_archivo.read())

# Leer y mostrar la primera línea
una_linea = mi_archivo.readline()
print(una_linea)
# Lee desde donde había dejado antes
una_linea = mi_archivo.readline()
print(una_linea)
# Lee desde donde había dejado antes
una_linea = mi_archivo.readline()
print(una_linea)

# como python detecta el salto de linea, una manera de quitarlo es con rstrip()
mi_archivo = open("prueba.txt")
una_linea = mi_archivo.readline()
# se va a visualizar pegado a la ultima linea mostrada
print(una_linea.rstrip())

# Nota: el archivo que se obtiene es una coleccion de strings, por lo tanto se
# pueden aplicar todos los métodos de los strings
mi_archivo = open("prueba.txt")
# por cada linea del archivo
for l in mi_archivo:
    #muestra
    print('Aqui dice: '+l)
    
# otra opcion es la siguiente y se recomienda solo hacerlo con archivos pequeños
mi_archivo = open("prueba.txt")
# me genera una lista con cada linea
todas = mi_archivo.readlines()
print(todas)

# Siempre que trabajemos con archivos, asegurarnos de tener el cierre del mismo para que se libere la memora usada en el
mi_archivo.close()