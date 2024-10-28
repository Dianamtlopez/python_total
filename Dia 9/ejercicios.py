#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

# Soluciones a las Prácticas del Día 9

# Antes de dar por finalizadas las prácticas del día de hoy y pasar al proyecto, 
# te comparto las posibles soluciones para cada una de las prácticas que fueron 
# propuestas el día de hoy, en caso de que hayas tenido alguna dificultad para terminarlas.

# ¡Ten en cuenta que estas soluciones no son únicas! Si has arribado por otro camino a un 
# código que arroja un resultado correcto en PyCharm o tu editor de código de preferencia, 
# quiero que sepas que has hecho un buen trabajo (no siempre pueden contemplarse todos los 
# casos a la hora de evaluar una tarea).

# Práctica Módulo Collections 1

from collections import Counter
 
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
 
contador = Counter(lista)

# Práctica Módulo Collections 2

from collections import defaultdict
 
mi_diccionario = defaultdict(lambda:"Valor no hallado")
mi_diccionario["edad"] = 44

# Práctica Módulo Collections 3

from collections import deque
 
lista_ciudades= deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

# Práctica Módulo Datetime 1

from datetime import date
 
mi_fecha = date(1999, 2, 3)

# Práctica Módulo Datetime 2

from datetime import date
 
hoy = date.today()

# Práctica Módulo Datetime 3

from datetime import datetime
 
minutos = datetime.now().minute

# Práctica Módulo Math 1

import math
 
resultado = math.log10(25)

# Práctica Módulo Math 2

import math
 
resultado = math.sqrt(math.pi)

# Práctica Módulo Math 3

import math
 
resultado = math.factorial(7)

# Práctica Módulo RE 1
 
import re
 
def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

# Práctica Módulo RE 2

import re
 
def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")

# Práctica Módulo RE 3

import re
 
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


# Recuerda que si tienes alguna duda que aún no quede resuelta, tienes a tu disposición el 
# espacio de Preguntas y Respuestas.

# Te veo en el proyecto!