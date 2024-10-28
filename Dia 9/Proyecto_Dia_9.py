#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

"""
Instrucciones:

Tu trabajo es crear un Buscador de Números de Serie. ¿Qué es eso? Es un programa que se encargue de buscar números de serie que cumplan un determinado formato, dentro de un arbol de carpetas.
Tu programa va a recorrer todos los archivos y subcarpetas de un directorio raiz (en este caso, la carpeta que acabas de descomprimir), y va a buscar cualquier string que coincida con un patrón de número de serie. Sabemos que no puede haber más de un número de serie por archivo.
Para lograrlo vas a usar el módulo os para abrir e iterear por el directorio, y las expresiones regulares para encontrar el formato de número de serie correcto.
A los fines de este ejercicio, estas son las condiciones de formato que deben cumplir los hallazgos:

- [N] + [tres carateres de texto] + [-] + [5 números]

Por ejemplo: Nryu-12365

La presentación en pantalla de los hallazgos debe ser un listado en formato de tabla, que respete el siguiente formato de ejemplo:

----------------------------------------------------
Fecha de búsqueda: [fecha de hoy]

ARCHIVO		NRO. SERIE
-------		----------
texto1.txt	Nter-15496
texto25.txt	Ngba-85235

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------

IMPORTANTE:
* La 'Duración de búsqueda' debe estar redondeada hacia arriba
* No olvides que la mejor forma de recorrer un arbol de carpetas, probablemente sea con el método walk() de os.
* Observa que la fecha de búsqueda debe ser la fecha del día en que ejecutes el código, por lo que necesitas echar mano del módulo datetime.
* Animate a encontrar una manera de mostrar la fecha de hoy con el formato dd/mm/aa.
* Para informar la duración de la búsqueda al final de tu presentación, vas a necesitar del módulo time.
* Recuerda que para poder imprimir todo en formato de tabla puedes usar los caracteres especiales \t para tabular.
"""

# manejo de carpetas y archivos
import os
# manejo de expresiones regulares
import re
# capturar datos del tiempo
import datetime
# Medir el tiempo
import time
# Redondear
import math

# descomprimir archivos con shutil
# shutil.unpack_archive('Proyecto+Dia+9.zip', 'Extraccion_Proyecto', 'zip')

# saber el directorio actual
# print(os.getcwd())

# Inicio_1 nos da la hora exacta del inicio de la ejecución
inicio_1 = time.time()

# Se establece la ruta a recorrer
ruta = 'D:\\Users\\diana\\Downloads\\PYTHON TOTAL\\python_total\\Dia 9\\Extraccion_Proyecto\\Mi_Gran_Directorio'

# Se selecciona el patrón deseado
patron = r'N\D{3}-\d{5}'

# Lista para almacenar resultados
resultados = []

def calcular_resultados():
    # Recorrer la estructura de carpetas usando os.walk
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        # Iteramos en los archivos
        for archivo in archivos:
            # Crear ruta completa para cada archivo
            ruta_archivo = os.path.join(carpeta, archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                for i, linea in enumerate(f):
                    # Buscar el patrón en cada línea del archivo
                    if re.findall(patron, linea):
                        # Adiciona a la lista resultados cada archivo con cada patrón encontrado
                        resultados.append({
                            "archivo": archivo,
                            "linea": i + 1,
                            "contenido": re.findall(patron, linea)
                        })
    return resultados

def mostrar_todo():
    # Obtenemos la fecha de hoy
    fecha = datetime.date.today()

    # Mostrar los resultados
    print('-' * 50)
    print(f'Fecha de búsqueda: [{fecha.day}-{fecha.month}-{fecha.year}]\n')
    print('  ARCHIVO\t NRO. SERIE  ')
    print('-----------  \t --------------')

    for resultado in resultados:
        print(f"{resultado['archivo']} \t {resultado['contenido']}")

    print(f'\nNúmeros encontrados: {len(resultados)}')

    # Final_1 nos da la hora exacta del fin de la ejecución
    final_1 = time.time()

    duracion = final_1 - inicio_1

    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')

    print('-' * 50)

# Ejecutar las funciones
calcular_resultados()
mostrar_todo()