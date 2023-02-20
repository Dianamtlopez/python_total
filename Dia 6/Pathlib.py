#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# pathlib nos permite hacer muchas cosas de manera eficiente
from pathlib import Path, PureWindowsPath

# Rutas interpretadas por cualquier sistema operativo con Path, no necesitamos ni abrir ni cerrar el archivo
carpeta = Path("D:/Users/User/Downloads/PYTHON_TOTAL/Dia 6/prueba.txt")
print(carpeta.read_text())

# Nombre del archivo
print(carpeta.name)
# Nos devuelve el tipo de archivo o la extension
print(carpeta.suffix)
# Nos entrega el nombre del archivo sin la extension
print(carpeta.stem)

if not carpeta.exists():
    print('El archivo, no existe')
else:
    print('Genial, el archivo, existe')

# transformar cualquier ruta a una en windows
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)