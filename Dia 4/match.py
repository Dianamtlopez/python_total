#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

# Funciona con python 3.10 en adelante
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

# Funciona con python 3.10 en adelante
cliente = {'nombre': 'Diana',
            'edad': 41,
            'ocupacion': 'instructor'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista': 'Kianu reeves',
                              'director': 'Lana y Lili Wachowsky'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
             print('Es un cliente')
             print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
             print("Es pelicula")
             print(titulo, protagonista, director)
        case _:
             print('No se que es esto')