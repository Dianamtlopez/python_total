#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

# ******************************************************
# Práctica Módulo RE 2
# Crea una función llamada verificar_saludo para verificar si una 
# frase entregada como argumento inicia con la palabra "Hola". Si se 
# encuentra el patrón, la función debe finalizar mostrando el mensaje 
# "Ok", pero si detecta que la frase no contiene "Hola", debe informarle 
# al usuario "No has saludado" imprimiendo el mensaje en pantalla.

import re

def verificar_saludo(frase):
    patron = r'^Hola'
    if re.match(patron, frase):
        return "Ok"
    else:
        return "No has saludado"

# llamado de la función
print(verificar_saludo("Hola, ¿cómo estás?"))  # imprime "