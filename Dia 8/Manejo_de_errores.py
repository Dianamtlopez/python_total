#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
def suma():
    n1 = int(input("Digite el primer número: "))
    n2 = int(input("Digite el segundo número: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)

try:
    # Código que queremos probar
    suma()
# except:
    # Código a ejecutar si hay un error
    # print("Algo no ha salido bien")"""
except TypeError:
    # Código a ejecutar si hay un error de tipo de datos
    print("Estas intentando concatenar 2 tipos distintos")
except ValueError:
    # Código a ejecutar si hay un error cuando se ingresa un caracter de texto en vez de uno numérico
    print("Estas intentando ingresar un dato que no es un número")
else:
    # Código que quiero ejecutar si no hay un error
    print("Hiciste todo bien!")
finally:
    # Código que se va a ejecutar de todos modos
    print("Eso fue todo")

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un número: "))
        except:
            print("Eso no es un número")
        else:
            print(f"Ingresaste el número {numero}")
            break
    print("Gracias")

pedir_numero()