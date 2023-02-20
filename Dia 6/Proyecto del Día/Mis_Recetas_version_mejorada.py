#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Módulos a importar
import os
from pathlib import Path
from os import system

# Creo la variable mas importante que va a obtener el path
mi_ruta = Path(Path.home(), 'Recetas')

# Me informa Cuantas recetas hay
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador
    
# Menú de inicio
def inicio():
    system('cls')
    # Dar primero la bienvenida al usuario
    cadena = 'HOLA, BIENVENIDO AL ADMINISTRADOR DE RECETAS!'.center(100, " ")
    sep = ('*'*102)
    print(f'{sep}\n*{cadena}*\n{sep}')
    print()
    print(f'Las recetas se encuentran en {mi_ruta}')
    print(f'Total recetas: {contar_recetas(mi_ruta)}')
    
    eleccion_menu = ''
    # verificamos que el ingreso sea un numero por mas que esté en un string
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range (1,7):
        print('Elige una opción: ')
        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa
        """)
        eleccion_menu = input()
    return (int(eleccion_menu))

def mostrar_categorias(ruta):
    print('Categorías: ')
    ruta_categorias = Path(ruta)
    lista_categorías = []
    contador = 1
    # Metodo Path iterdir(), permite iterar dentro del directorio pasando por sus elemenetos
    for carpeta in ruta_categorias.iterdir():
        # Asignamos solo el nombre de las carpetas encontradas
        carpeta_str = str(carpeta.name)
        # Enumeramos las carpetas, las mostramos y damos la opción de elegir
        print(f"[{contador}] - {carpeta_str}")
        # A la lista lista_categorías, se asigna la ruta para llegar hasta alli
        lista_categorías.append(carpeta)
        contador += 1
    return lista_categorías
        
def elegir_categoria(lista):
    eleccion_correcta = ''
    # Se repite hasta que ingrese un numero entre 1 hasta la cantidad de categórias
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input('\nElige una categoríe: ')
    
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = ''
    # Se repite hasta que ingrese un numero entre 1 hasta la cantidad de recetas
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,len(lista) + 1):
        eleccion_receta = input('\nElige una receta: ')
    
    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))
    
def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        # se va escribiendo o copiando linea a linea
        crea_archivo = ''
        while True:
            inputs = input()
            if inputs:
                crea_archivo += inputs + '\n'
            else:
                break
        contenido_receta = crea_archivo
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name}, ha sido eliminada correctamente.')
    
def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(F"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = ''
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPresione v para volver al menu: ')

finalizar_programa = False

while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        # Mostrar categorías
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir categoría
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            # elegir recetas
            mi_receta = elegir_recetas(mis_recetas)
            # Leer receta
            leer_receta(mi_receta)
        # volver inicio
        volver_inicio()
    elif menu == 2:
        # mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        # crear receta nueva
        crear_receta(mi_categoria)
        # volver inicio
        volver_inicio()
    elif menu == 3:
        # crear categoría
        crear_categoria(mi_ruta)
        # volver inicio
        volver_inicio()
    elif menu == 4:
        # Mostrar categorías
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir categoría
        mi_categoria = elegir_categoria(mis_categorias)
        # mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        # elegir recetas
        mi_receta = elegir_recetas(mis_recetas)
        # eliminar receta
        eliminar_receta(mi_receta)
        # volver inicio
        volver_inicio()
    elif menu == 5:
        # Mostrar categorías
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir categoría
        mi_categoria = elegir_categoria(mis_categorias)
        print()
        # eliminar categorias
        if len(mostrar_recetas(mi_categoria)) > 0:
            print("\nhay recetas en esta categoría, para eliminar la categoría, debes eliminar primero la receta.")
        else:
            eliminar_categoria(mi_categoria)        
        # volver inicio
        volver_inicio()
    elif menu == 6:
        # Finalizar programa
        finalizar_programa = True
        