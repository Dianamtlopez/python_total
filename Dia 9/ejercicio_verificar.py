#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

# **************************************************************
# Práctica Módulo RE 3
# El código postal de una región determinada se forma a partir de dos caracteres 
# alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una función, 
# llamada verificar_cp para comprobar si el código postal pasado como argumento sigue 
# este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: 
# "El código postal ingresado no es correcto".
# **************************************************************

import re

def verificar_cp(cp):
    patron = r'[[A-Za-z]{2}\d{4}$'
    if re.match(patron, cp):
        return "Ok"
    else:
        return "El código postal ingresado no es correcto"

# Llamado de la función
print(verificar_cp("sa3900"))