#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

# Expresiones regulares
# caracteres especiales         ejemplo         resultado
# \d dígito numérico            v\d.\d\d        v1.02   -   v2.03
# \w caracter alfanumérico      \w\w\w-\w\w     sol-do  -   ABC-25
# \s espacio en blanco          número\s\d\d    número 25   - número 99
# \D no es numérico             \D\D\D\D        abcd    -   AB-C
# \W no es alfanumérico "signos" \W\W\W         +=-     -   !*?
# \S no es espacio en blanco    \S\S\S\S        1234    -   abcd
# \b palabra completa           \b\w\w\w\b      cat     -   copa
# \B palabra incompleta         \B\w\w\w\B      ca      -   cop

# Caracteres Cuantificadores, que significa que no tenemos que reoetir los 
# caracteres especiales varias veces
# \d{3}-\d{3}-\d{4} 
# caracteres especiales                             ejemplo         resultado
# + un caracter especial aparece una o más veces    código_\d-\d+   código_5-5  -   código_5-555
# {n} se repite n veces                             \d-\d{4}        1-0000      -   5-6060
# {n,m} se repite de n a m veces                    \w{3,5}         hola    -   sol - mundo
# {n, } desde ne hacia arriba                       -\d{4,}-        -11111111-  -   -00000-     -   -001555321512332213-
# * significa cero o más                            \w\s*\w         significa que el espacio existe una, muchas o ninguna vez
# ? el caracter aparece una vez o ninguna           casas?          casa    -   casas

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra) # True

# con las expresiones regulares
import re

patron = "nada"

busqueda = re.search(patron, texto)
print(busqueda) # None

patron = "ayuda"

busqueda = re.search(patron, texto)
print(busqueda) 

# ubicación de la palabra
print(busqueda.span()) 
# ubicación del comienzo
print(busqueda.start())
# ubicación del final
print(busqueda.end())

# encontrar todas
busqueda = re.findall(patron, texto)
print(busqueda) 
# largo
print(len(busqueda))

# encontrar cada hallazgo
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

# *************************************************************
# Construcción de pastrones especiales
texto = "Llamar al 564-525-6588 ya mismo"

patron = r'\d\d\d-\d\d\d-\d\d\d\d'

resultado = re.search(patron, texto)
print(resultado) 

# obtener el deto en particular
print(resultado.group())

# busqueda con cuantificadores
patron1 = r'\d{3}-\d{3}-\d{4}'
resultado1 = re.search(patron1, texto)
print(resultado1) 
# obtener el deto en particular
print(resultado1.group())

# cuando quiero seleccionar una parte del texto
patron2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado2 = re.search(patron2, texto)
print(resultado2.group(3)) 

# ejemplos de usos
clave = input("Clave:")

# control del formato con la clave del usuario
# \D{1} que no sea numérico y que se escriba una vez
# \w{7} que sea alfanumérico y se repita 7 veces
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)
print(chequear)

# operadores especiales
texto = 'No atendemos los lunes por la tarde'
buscar = re.search(r'lunes|martes', texto)
print(buscar)

# los por cada punto al inicio o al final, nos muestra los caracteres q alli se encuentren
buscar = re.search(r'...demos...', texto)
print(buscar)

# el acento circunflejo nos indica si un patron se encuentra al comienzo del string
buscar = re.search(r'^\D', texto)
print(buscar)

# el signo pesos nos indica si un patron se encuentra al final del string
buscar = re.search(r'\D$', texto)
print(buscar)

# Esto significa que el patrón lo debe excluir [^]
buscar = re.findall(r'[^\s]', texto)
print(buscar)

# Esto significa que el patrón lo debe excluir [^] y el signo mas dice q una o más veces
buscar = re.findall(r'[^\s]+', texto)
print(buscar)

# muestra todo el texto sin espacios vacíos
print(''.join(buscar))

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

def erificar_email():
    email = input("Ingrese su email: ")
    patron = r'[^\D]+@[\D]+[.com]$|[^\D]+@[\D]+[.com.\D\D]$'
    chequear = re.search(patron, email)
    return chequear

print(erificar_email())
# ***************************************************************


