#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Práctica Abrir y Manipular Archivos 1
# Abre el archivo prueba.txt e imprime su contenido.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código

mi_archivo = open("prueba.txt")
print(mi_archivo.read())

# Práctica Abrir y Manipular Archivos 2
# Imprime la primera línea del archivo prueba.txt
# No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
mi_archivo = open("prueba.txt")
una_linea = mi_archivo.readline()
print(una_linea)
mi_archivo.close()

# Práctica Abrir y Manipular Archivos 3
# Abre el archivo prueba.txt e imprime únicamente la segunda línea.
mi_archivo = open("prueba.txt")
una_linea = mi_archivo.readline()
una_linea = mi_archivo.readline()
print(una_linea)
mi_archivo.close()