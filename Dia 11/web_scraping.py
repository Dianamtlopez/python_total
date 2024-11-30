#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

# print(type(resultado))
# print(resultado.text)

# bs4 se usa para buscar elementos en la página web y extraer texto de la página web
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Obtener El texto de lo que se desea buscar
# parrafo_especial = sopa.select('p')[3].getText()
# print(parrafo_especial)

# Obtener todo lo que se encuentra dentro de la clase
columna_lateral = sopa.select('.container div')

for d in columna_lateral:
    print(d.getText())