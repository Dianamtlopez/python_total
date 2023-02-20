#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
import os
from pathlib import Path

# Retorna una cadena de bytes que representa el directorio de trabajo actual
ruta = os.getcwd()
print(ruta)

# Permite ingresar la ruta donde se encuentra el archivo
ruta = os.chdir("D:\\Users\\User\\Downloads\\PYTHON_TOTAL\\Dia 6\\Alternativo")
# Crea un objeto y lo asigna a la variable archivo
archivo = open("otro_archivo.txt")
# Para leer el archivo
print(archivo.read())

# Permite crear nuevos directorios
# ruta = os.makedirs("D:\\Users\\User\\Downloads\\PYTHON_TOTAL\\Dia 6\\Alternativo\\Nueva_Carpeta")

# Obtener tanto archivo como directorio
ruta = "D:\\Users\\User\\Downloads\\PYTHON_TOTAL\\Dia 6\\prueba.txt"
# Obtiene el nombre de base de la ruta o sea el archivo
elemento = os.path.basename(ruta)
print(elemento)

# Obtiene el directorio o primera parte de la ruta
elemento = os.path.dirname(ruta)
print(elemento)

# Obtiene ambos elementos separados por una tupla
elemento = os.path.split(ruta)
print(elemento)

# Para eliminar carpetas
#os.rmdir("D:\\Users\\User\\Downloads\\PYTHON_TOTAL\\Dia 6\\Alternativo\\Nueva_Carpeta")

# otra manera de leer archivos sin os
otro_archivo = open("D:\\Users\\User\\Downloads\\PYTHON_TOTAL\\Dia 6\\Alternativo\\otro_archivo.txt")
print(otro_archivo.read())

# Rutas interpretadas por cualquier sistema operativo
carpeta = Path("D:/Users/User/Downloads/PYTHON_TOTAL/Dia 6/Alternativo")
# Concatenación para crear rutas
archivo = carpeta / "otro_archivo.txt"
mi_archivo = open(archivo)
print(mi_archivo.read())

# Otra manera abreviada
carpeta = Path("/Users/User/Downloads/PYTHON_TOTAL/Dia 6/Alternativo") / "otro_archivo.txt"
mi_archivo = open(carpeta)
print(mi_archivo.read())

