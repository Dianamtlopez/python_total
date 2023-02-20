#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Práctica Generadores 1
# Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia 
# infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez 
# que sea llamada mediante next.

def secuencia_infinita():
    x = 1
    while True:
        yield x
        x += 1
        

generador = secuencia_infinita()

print(next(generador))
print(next(generador))


# Práctica Generadores 2
# Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera 
# indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva 
# el siguiente múltiplo (7, 14, 21, 28...).


def multiplos_indefinidos():
    x = 1
    while True:
        yield x * 7
        x += 1

generador = multiplos_indefinidos()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

# Práctica Generadores 3
# Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un 
# mensaje cada vez que sea llamado:

# "Te quedan 3 vidas"
# "Te quedan 2 vidas"
# "Te queda 1 vida"
# "Game Over"

# Almacena el generador en la variable perder_vida

def vidas_personaje():
    x = 3
    while x >= 0: 
        if x == 3 or x == 2:
            yield f"Te quedan {x} vidas"
        if x == 1:
            yield f"Te queda {x} vida"
        if x == 0:
            yield "Game Over"
        x -= 1


perder_vida = vidas_personaje()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))

