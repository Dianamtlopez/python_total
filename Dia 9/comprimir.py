#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

import zipfile

# Comprimir archivos
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()

# Descomprimir archivos
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()

import shutil
# Comprimir con shutil
carpeta_origen = "D:\\Users\\diana\\Desktop\\carpeta_superior"

# Nombre de la carpeta comprimida
archovo_destino = 'Todo_Comprimido'

shutil.make_archive(archovo_destino, 'zip', carpeta_origen)

# descomprimir archivos con shutil
shutil.unpack_archive('Todo_Comprimido.zip', 'Etraccion_Terminada', 'zip')
