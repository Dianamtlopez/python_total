#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

import os
from pathlib import Path
from os import system
from os import remove

def bienvenida():
    """
        Recetario
        se saluda al usuario, se muestra la ruta que almacena las recetas, se informa 
        con cuantas recetas se cuenta actualmente
    """
    system('cls')
    # Dar primero la bienvenida al usuario
    cadena = 'HOLA, BIENVENIDO AL RECETARIO!'.center(100, " ")
    sep = ('*'*102)
    print(sep)
    print(cadena)
    print(sep)
    
    # Informar la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas 
    # Obtiene el path raiz
    base = Path.home()
    # Se crea una ruta absoluta que va hasta la carpeta Recetas
    guia = Path(base, "Recetas")
    print(f'\nEn la siguiente ruta, encontrarás las recetas con las que contamos actualmente:\n- {guia}')
    # informar cuántas recetas hay en total dentro de esa carpeta
    # Esto hace que se incluyan carpetas y sub carpetas y enumere todos los txt que encuentre
    cont = 0
    for txt in Path(guia).glob('**/*.txt'):
        cont += 1

    print(f'\nActualmente contamos con {cont} Recetas.\n')

    # Pedir que elija una de las siguientes opciones
    # Funciona con python 3.10 en adelante

    print('Opciones:')
    print('1. Leer Receta.')
    print('2. Crear Receta.')
    print('3. Crear Categoría.')
    print('4. Eliminar Receta.')
    print('5. Eliminar Categoría.')
    print('6. Salir.')

def Listar_carpetas():
    """
        Funcioón que devuelve en forma de lista las carpetas encontradas en la ruta relativa creada por
        ruta = Path(base, "Recetas")
    """
    # Obtiene el path raiz
    base = Path.home()
    # Se crea una ruta absoluta que va hasta la carpeta Recetas
    ruta = Path(base, "Recetas")
    return ruta

def listar_archivos(ruta):
    """
        Funcioón que devuelve en forma de lista los archivos .txt encontrados en la ruta relativa creada por
        guia = Path(base, "Recetas", ruta)
    """
    # Obtiene el path raiz
    base = Path.home()
    # Se crea una ruta absoluta que va hasta la carpeta seleccionada
    guia = Path(base, "Recetas", ruta)
    elemento = []
    for txt in Path(guia).glob('*.txt'):
        elemento.append(os.path.basename(txt))
    return elemento

def obtener_ruta(ruta, archivo):
    """
        Funcioón que devuelve la ruta relativa creada por
        guia = Path(base, "Recetas", ruta, archivo)
    """
    # Obtiene el path raiz
    base = Path.home()
    # Se crea una ruta absoluta que va hasta la carpeta seleccionada
    guia = Path(base, "Recetas", ruta, archivo)
    return guia

def crear_carpeta(carpeta):
    """
        Funcioón que recibe por argumento, el nombre de una carpeta
        y con este nombre crea la carpeta
    """
    # trae la ruta absoluta obtenida en Listar_carpetas()
    # Concatena la carpeta que se desea crear a la ruta obtenida
    ruta = Path(Listar_carpetas(), carpeta)
    # Permite crear nuevos directorios
    n_carpeta = os.makedirs(ruta)
    print('Categoría creada correctamente.\n')
    return ruta

def eliminar_archivo(carpeta, archivo):
    """
        Funcioón que recibe por argumento, el nombre de un archivo
        y con este nombre elimina dicho archivo
    """
    # trae la ruta absoluta obtenida en Listar_carpetas()
    # Concatena la carpeta que se desea crear a la ruta obtenida
    ruta = Path(Listar_carpetas(), carpeta, archivo)
    # Permite Borrar un archivos
    n_carpeta = os.remove(ruta)
    print('Archivo eliminado correctamente.\n')
    return ruta

def eliminar_carpeta(carpeta):
    """
        Funcioón que recibe por argumento, el nombre de una carpeta
        y con este nombre elimina la carpeta
    """
    # trae la ruta absoluta obtenida en Listar_carpetas()
    # Concatena la carpeta que se desea crear a la ruta obtenida
    ruta = Path(Listar_carpetas(), carpeta)
    # Permite eliminar un directorio
    n_carpeta = os.rmdir(ruta)
    print('Categoría eliminada correctamente.\n')
    return ruta
    
# Función de más alto nivel
def main():
    """
        Se hace llamado a las diferentes funciones que permiten la ejecucion de
        la implementación de un recetario
    """
    # Llamado al menú
    bienvenida()
    print()
    seleccion = 0
    while seleccion not in range(1,7):
        seleccion = int(input('Ingresa la opcion deseada: '))
    
    seleccion = str(seleccion)
    # Cada vez que el usuario ingrese una opción errada, se limpia la pantalla y vuelve a mostrar el contenido
    system('cls')
    match seleccion:
        case '1':
            print('\nLectura de Recetas:\n')
            # Funcion que recibe como argumento una ruta del sistema de ficheros y devuelve una lista 
            contenido = os.listdir(Listar_carpetas())
            for dir in contenido:
                # Visualizar carpetas que contiene
                print(dir)

            print()
            categoria = ''
            while categoria not in contenido:
                categoria = input('Digite la categoria deseada: ')
            else:
                print()
                # Obtiene el nombre de base de la ruta o sea el archivo
                archivo = listar_archivos(categoria)
                for receta in archivo:
                    # Visualizar archivos
                    print(receta)
            
            print()
            nombre_arch = ''
            while nombre_arch not in archivo:  
                nombre_arch = input('Digite la Receta que desea visualizar: ')
            else:
                print()
                mi_archivo = open(obtener_ruta(categoria, nombre_arch))
                print(mi_archivo.read())
                mi_archivo.close()
            
        case '2':
            print('\nCrear nuevas Recetas:\n')
            # Funcion que recibe como argumento una ruta del sistema de ficheros y devuelve una lista 
            contenido = os.listdir(Listar_carpetas())
            for dir in contenido:
                # Visualizar carpetas que contiene
                print(dir)

            print()
            categoria = ''
            while categoria not in contenido:
                categoria = input('Digite la categoria deseada: ')
            else:
                print()
                # Obtiene el nombre de base de la ruta o sea el archivo
                archivo = listar_archivos(categoria)
                for receta in archivo:
                    # Visualizar archivos
                    print(receta)
            
            print()
            nombre_arch = ''
            while nombre_arch.find('.txt') == -1:  
                nombre_arch = input('Digite el nombre de la Receta que desea crear terminado en .txt: ')
            else:
                print()
                # para escribir en el archivo, hay dos formas si le coloco w, el archivo es reemplazado por el nuevo texto
                # y si no existe, solo se va a crear
                mi_archivo = open(obtener_ruta(categoria, nombre_arch), 'w')
                print('Digita la receta deseada: ')
                # se va escribiendo o copiando linea a linea
                crea_archivo = ''
                while True:
                    inputs = input()
                    if inputs:
                        crea_archivo += inputs + '\n'
                    else:
                        break
                # se agregan todos los inputs a mi_archivo
                mi_archivo.write(crea_archivo)
                mi_archivo.close()
            
        case '3':
            print('\nCrear categoría de Recetas:\n')
            # Funcion que recibe como argumento una ruta del sistema de ficheros y devuelve una lista 
            contenido = os.listdir(Listar_carpetas())
            for dir in contenido:
                # Visualizar carpetas que contiene
                print(dir)

            print()
            categoria = ''
            # Evalúo que se haya ingresado un nombre a la variable
            while len(categoria) == 0:
                categoria = input('Digite la categoría que deseada crear: ')
                contenido = os.listdir(Listar_carpetas())
                while categoria in contenido:
                    # Obtiene el nombre de base de la ruta o sea el archivo
                    print('Error, la categoría que desea crear ya existe!')
                    categoria = input('Digite Nuevamente la categoría que deseada crear: ')
                
                # Llamado a la funcion crear_carpeta
                archivo = crear_carpeta(categoria)
                # Mostrar carpetas existentes
                system('cls')
                print('Categorías creadas actualmente:\n')
                contenido = os.listdir(Listar_carpetas())
                for dir in contenido:
                    # Visualizar carpetas que contiene
                    print(dir)

        case '4':
            print('\nEliminar una Receta:\n')
            # Funcion que recibe como argumento una ruta del sistema de ficheros y devuelve una lista 
            contenido = os.listdir(Listar_carpetas())
            for dir in contenido:
                # Visualizar carpetas que contiene
                print(dir)

            print()
            categoria = ''
            while categoria not in contenido:
                categoria = input('Digite la categoria deseada: ')
            else:
                print()
                # Obtiene el nombre de base de la ruta o sea el archivo
                archivo = listar_archivos(categoria)
                for receta in archivo:
                    # Visualizar archivos
                    print(receta)
                print()
            
            nombre_arch = ''
            # Evalúo que se haya ingresado un nombre a la variable
            while len(nombre_arch) == 0:
                nombre_arch = input('Digite la receta que deseada eliminar: ')
                archivo = listar_archivos(categoria)
                while nombre_arch not in archivo:
                    # Obtiene el nombre de base de la ruta o sea el archivo
                    print('Error, la receta que desea eliminar no existe!')
                    nombre_arch = input('Digite Nuevamente la receta que desea eliminar: ')

                # Llamado a la funcion eliminar archivo
                archivo = eliminar_archivo(categoria, nombre_arch)
                # Mostrar carpetas existentes
                system('cls')
                print('Recetas actualizadas:\n')
                archivo = listar_archivos(categoria)
                for receta in archivo:
                    # Visualizar archivos
                    print(receta)
                print()

        case '5':
            print('\nEliminar categoría de Recetas:\n')
            # Funcion que recibe como argumento una ruta del sistema de ficheros y devuelve una lista 
            contenido = os.listdir(Listar_carpetas())
            for dir in contenido:
                # Visualizar carpetas que contiene
                print(dir)

            print()
            categoria = ''
            # Evalúo que se haya ingresado un nombre a la variable
            while len(categoria) == 0:
                categoria = input('Digite la categoría que deseada eliminar: ')
                contenido = os.listdir(Listar_carpetas())
                while categoria not in contenido:
                    # Obtiene el nombre de base de la ruta o sea la carpeta
                    print('Error, la categoría que desea eliminar no existe!')
                    categoria = input('Digite Nuevamente la categoría que deseada eliminar: ')
                
                # Llamado a la funcion eliminar_carpeta
                archivo = eliminar_carpeta(categoria)
                # Mostrar carpetas existentes
                system('cls')
                print('Categorías actualizadas:\n')
                contenido = os.listdir(Listar_carpetas())
                for dir in contenido:
                    # Visualizar carpetas que contiene
                    print(dir)

        case '6':
            print("Usted ha elegido salir...")
            quit()           
        case _:
            print("Opcion no encontrada.")

    print()
    input('Presiona enter para continuar: ')
    main()
    
# Se ejecuta el main.   
main()