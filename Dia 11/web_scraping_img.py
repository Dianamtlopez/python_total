#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/courses")

# bs4 se usa para buscar elementos en la página web y extraer texto de la página web
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Resolvemos la forma en la cual, vamos a encontrar las imagenes
# En este caso, vamos a buscar todas las imagenes que estan en la clase class="course-box-image"
# las cuales contienen las imagenes de los cursos
imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

# para descargar la imegen
imsgen_curso_1 = requests.get(imagenes)

# La función open abre un archivo en la ruta especificada (Dia 11\\mi_imagen.jpg) para trabajar con él.
# El argumento 'wb' indica:
# w: Modo de escritura ("write"). Esto sobrescribe el archivo si ya existe. Si no existe, se crea
# uno nuevo.
# b: Modo binario ("binary"). Esto es útil para manejar datos no textuales, como imágenes, archivos 
# de video, audio, etc.
# f se convierte en un objeto archivo que puede ser usado para escribir datos binarios en el archivo 
# mi_imagen.jpg.

f = open('Dia 11\\mi_imagen.jpg', 'wb')


# Copiamos el texto de la forma binaria en el archivo que creamos mi_imagen.jpg
f.write(imsgen_curso_1.content)
# Cierra el archivo
f.close()
