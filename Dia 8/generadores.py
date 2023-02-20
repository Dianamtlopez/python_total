#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Funcion Normal
def mi_funcion():
    return 4


# Generador yield quiere decir producir
def mi_generador():
    yield 4


print(mi_funcion())
# Nos dice que hay un objeto en algun lugar
print(mi_generador())

# Para poder visualizar el generador, hacemos lo siguiente:
g = mi_generador()


print(next(g))

# ahora mas complejo:
# Funcion Normal
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista


# Generador
def mi_generador():
    for x in range(1,5):
        yield x * 10


print(mi_funcion())
# Nos dice que hay un objeto en algun lugar
print(mi_generador())

# Para poder visualizar el generador, hacemos lo siguiente:
g = mi_generador()


print(next(g))
print(next(g))
print(next(g))
print(next(g))


def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))

# Básicamente, el generador recuerda donde quedó y contunúa alli en el próximo llamado 
