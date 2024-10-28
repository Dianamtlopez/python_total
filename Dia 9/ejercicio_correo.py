v#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

# ***************************************************************
# Práctica Módulo RE 1
# Crea una función llamada verificar_email para comprobar si una dirección 
# de email es correcta, que verifique si el email dado como argumento contiene
# "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque 
# aceptando también casos que cuentan con un dominio adicional, tal como 
# ".com.br" para el caso de un usuario de Brasil).

# Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el 
# mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, 
# debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.

# con las expresiones regulares
import re

def verificar_email(email):
    # Expresión regular corregida
    patron = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|com\.[a-zA-Z]{2})$'
    
    # Verifica si el email coincide con el patrón
    print(re.match(patron, email))
    if re.match(patron, email):
        return("Ok")
    else:
        return("La dirección de email es incorrecta")
        

# Llamada a la función
# verificar_email(input("Ingrese su email: "))

print(verificar_email("dianamtlopez@hotmai.lcom"))
# Llamada a la función para hacer pruebas
print(verificar_email("usuario@host.com"))          # Ok
print(verificar_email("usuario@host.com.br"))       # Ok
print(verificar_email("usuario@hostcom"))           # La dirección de email es incorrecta
print(verificar_email("usuario@host.comm"))         # La dirección de email es incorrecta
print(verificar_email("usuario@host.commmm"))       # La dirección de email es incorrecta

# ^[A-Za-z0-9._%+-]+: Acepta el nombre de usuario del correo, permitiendo caracteres alfanuméricos, 
# puntos (.), guiones (-), porcentajes (%), y más.
# @: Verifica la presencia del símbolo arroba (@).
# [A-Za-z0-9.-]+: Acepta el dominio principal, permitiendo caracteres alfanuméricos y puntos.
# \.(com|com\.[a-zA-Z]{2})$: Asegura que el correo termine exactamente en .com o .com. seguido de 
# dos letras, como en dominios geográficos (por ejemplo, .com.br).