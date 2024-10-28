#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

import os

# saber el directorio actual
# print(os.getcwd())

# creamos un archivo y le damos permisos de escritura
archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

# ver los archivos que tenemos
print(os.listdir())

# para mover archivos importamos la librería shutil
import shutil
# método para mover
# shutil.move('curso.txt' , "D:\\Users\\diana\\Desktop")

# Para eliminar archivos hay tres maneras de hacerlo, dos con os
# con os.unlink se elimina un archivo en una ruta que le demos
# con os.rmdir elimina una carpeta vacía que se encuentre en una ruta que le demos
# con shutil.rmt elimina todo lo que se encuentre en una ruta que yo le de, tener 
# cuidado con este método pues elimina todo lo que contenga la carpeta

# una alternativa es con send2trash
import send2trash
# eliminar archivo
send2trash.send2trash('curso.txt')

# con walk recorre todos los directorios, carpetas y sub carpetas dadas en una ruta
print(os.walk("D:\\Users\\diana\\Desktop"))

# como se nos genera un objeto podemos verlo con un iterador
# se va a crear tuplas con carpetas, sub carpetas y archivos
ruta = "D:\\Users\\diana\\Desktop\\LUPA"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print('Las subcarpetas son:')
    # iteramos en las subcarpetas
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    # iteramos en los archivos
    for arch in archivo:
        # puedo agregar la condicion si el archivo cumple con alguna condicion
        # en este caso voy a pedir los que inicien con Dic
        if arch.startswith('Dic'):
            print(f'\t{arch}')
    print('\n')

# Notas:

# Por lo general, querrás evitar cualquier paso en falso utilizando el método rmtree()
#  del módulo shutil, ya que los archivos se eliminan sin dejar rastros ni pasar por la 
# papelera de reciclaje, por lo que no podrás recuperar tu información si te equivocas.

# Tanto unlink() como rmdir() pertenecen al módulo os. La diferencia radica en que el 
# primero elimina un archivo del directorio indicado, y el segundo elimina una carpeta vacía.

# El módulo Send2Trash debe ser instalado externamente ya que no pertenece a los módulos 
# incorporados de Python