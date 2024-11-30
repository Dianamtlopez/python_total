#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

import bs4
import requests

# Crear una Url sin número de página
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Ver todas las páginas
'''
for n in range(1,51):
    print(url_base.format(n))
'''

# Crear una lista con todas las urls que tengan 4 o 5 estrellas
titulos_rating_alto = []

# Iterar pàginas
for pagina in range(1,51):

    # Crear la sopa para cada página
    url_pagina = url_base.format(pagina)
    # Creamos el request
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Selección de los datos con los libros
    libros = sopa.select('.product_pod')
    
    # Iterar en los libros
    # Selección que me confirma si la lista tiene elementos: libros[0].select('.star-rating.Three')
    # Tomo el título del libro, cómo aparecen varias a, selecciono la segunda, pues es la que 
    # obtiene el título del libro: libros[0].select('a')[1]['title']
    # Ahora debo hacer un loop for que recorra todas las páginas de los libros, que mire todo los libros,
    # que luego se fije si ese libro tiene 4 o 5 estrellas y finalmente que tome el título del libro
    
    for libro in libros:
        # Chequear que los libros tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # Tomar el título del libro y lo guardamos en una variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregamos el libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Ver los libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)

