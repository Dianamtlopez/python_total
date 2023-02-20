#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTODAD:             * UDEMY                       *
#******************************************************
"""
Crear el tunero para una farmacia que tiene tres áreas de atención:
- Perfumería.
- Farmacia (que es donde venden los medicamentos).
- Cosméticos. 
Preguntar al cliente a cuál de las áreas desea dirigirse, y le va a dar un número de
turno según a qué área se dirija. 
Por ejemplo, si elige cosmética, le va a dar el número C-54 (“C” de cosmética). 
Luego de eso, nos va a preguntar si queremos sacar otro turno. 
Esto, en realidad, es para simular si viene un nuevo cliente. Y repetirá todo el proceso.
"""
from colored import fg, bg, attr, stylize
# fg = Color del frente
# bg = Color del fondo
# attr = Atributo
color = fg(57) + bg(1) + attr(1)
res = attr(0)
linea = ("*" * 26)
lateral = ("*                        *")


# Se crea una función para los generadores y se retorna dependiendo el turno solicitado
def perfumeria():

    x = 0
    while True:
        if x < 100:
            # Para colocar ceros a la izquierda para completar 2 cifras (str(x).zfill(2))
            yield f"P-{str(x).zfill(2)}"
            x += 1
        else:
            x = 0


def farmacia():

    x = 0
    while True:
        if x < 100:
            # Para colocar ceros a la izquierda para completar 2 cifras (str(x).zfill(2))
            yield f"F-{str(x).zfill(2)}"
            x += 1
        else:
            x = 0


def cosmeticos():

    x = 0
    while True:
        if x < 100:
            # Para colocar ceros a la izquierda para completar 2 cifras (str(x).zfill(2))
            yield f"C-{str(x).zfill(2)}"
            x += 1
        else:
            x = 0


# Se crea el texto que tendrá el decorador
def decorar_turno(funcion):

    def turno_decorado(operacion):
        print(color + linea + res)
        print(color + "* Su turno es:           *" + res)
        print(color + lateral + res)
        funcion(color + f'*         {operacion}           *' + res)
        print(color + lateral + res)
        print(color + '* Espere y será atendido *' + res)
        print(color + linea + res)
    return turno_decorado


# Se crea la funcion a realizar por el decorador, en este caso será imprimir todo el texto que se reciba
def turno_seleccionado(texto):
        print(texto)

