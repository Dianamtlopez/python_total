<<<<<<< HEAD
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
class Pajaro:

    # Atributos de clase
    alas = True
    
    # Constructor
    def __init__(self, color, especie):
        # Self significa que hace referencia a atribitos de la propia clase 
        self.color = color
        self.especie = especie

# instancia de la clase
mi_pajaro = Pajaro('Negro', 'Tucan')
print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}.')

# Para consultar atributos de clase, no necesito instanciar
print(Pajaro.alas)
# Tambien lo puedo consultar desde el objeto ya que todos los objetos van a tener estos atributos
print(mi_pajaro.alas)

# Práctica Atributos 1
# Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
# Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('Blanco', 4)
print(casa_blanca.color, casa_blanca.cantidad_pisos)

# Práctica Atributos 2
# Crea una clase llamada Cubo, y asígnale el atributo de clase:
# caras = 6
# y el atributo de instancia:
# color
# Crea una instancia cubo_rojo, de dicho color.

class Cubo:

    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')

# Práctica Atributos 3
# Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
# real = False
# Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
# especie = "Humano"
# magico = True
# edad = 17

class Personaje:

    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)
=======
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTODAD:             * UDEMY                       *
#******************************************************
class Pajaro:

    # Atributos de clase
    alas = True
    
    # Constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

# instancia de la clase
mi_pajaro = Pajaro('Negro', 'Tucan')
print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}.')

# Para consultar atributos de clase, no necesito instanciar
print(Pajaro.alas)
# Tambien lo puedo consultar desde el objeto ya que todos los objetos van a tener estos atributos
print(mi_pajaro.alas)

# Práctica Atributos 1
# Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
# Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('Blanco', 4)
print(casa_blanca.color, casa_blanca.cantidad_pisos)

# Práctica Atributos 2
# Crea una clase llamada Cubo, y asígnale el atributo de clase:
# caras = 6
# y el atributo de instancia:
# color
# Crea una instancia cubo_rojo, de dicho color.

class Cubo:

    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')

# Práctica Atributos 3
# Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
# real = False
# Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
# especie = "Humano"
# magico = True
# edad = 17

class Personaje:

    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)
>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
