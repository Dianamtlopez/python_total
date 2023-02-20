#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
# y devuelva su contenido (read).

def abrir_leer(archivo):
    mi_archivo = open(archivo)
    # Leer y mostrar todo el archivo
    return(mi_archivo.read())

archivo = "prueba.txt"
abrir_leer(archivo)

# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(archivo):
    archivo = open(archivo,'w')
    archivo.write("contenido eliminado")

# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
# y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
# Finalmente, debe cerrar el archivo abierto.

def registro_error(archivo):
    archivo = open(archivo, 'a')
    archivo.write("se ha registrado un error de ejecución\n")
    archivo.close()