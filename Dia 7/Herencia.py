<<<<<<< HEAD
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

# Hereda de la clase animal
class Pajaro(Animal):
    print('Este animal se llama Piolin')

# instancia de Pajaro
piolin = Pajaro(2, 'Amarillo')
# piolin ha heredado el método de animal
piolin.nacer()
print(piolin.color)

# Indica de quien hereda la clase
print(Pajaro.__bases__)

# Indica que sub clases tiene
print(Animal.__subclasses__())

# Práctica Herencia 1
# Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: 
# nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    print(f'Alumno')

informacion = Alumno('Diana', 41)
print(informacion.nombre)

# Práctica Herencia 2
# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: 
# edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.

class Mascota:

    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    
    print(f'La mascota es un Perro.')

datos = Perro(7, 'Luna', 4)
print(f'La mascota tiene {datos.cantidad_patas} patas, se llama {datos.nombre} y tiene {datos.edad} años.')


# Práctica Herencia 3
# Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los 
# métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.

class Vehiculo:

    def acelerar(self):
        print('Acelero')

    def frenar(self):
        print('Freno')

class Automovil(Vehiculo):
    print('Soy un automóvil que: ')

info = Automovil()
info.acelerar()
info.frenar()
=======
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTODAD:             * UDEMY                       *
#******************************************************
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

# Hereda de la clase animal
class Pajaro(Animal):
    print('Este animal se llama Piolin')

# instancia de Pajaro
piolin = Pajaro(2, 'Amarillo')
# piolin ha heredado el método de animal
piolin.nacer()
print(piolin.color)

# Indica de quien hereda la clase
print(Pajaro.__bases__)

# Indica que sub clases tiene
print(Animal.__subclasses__())

# Práctica Herencia 1
# Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: 
# nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    print(f'Alumno')

informacion = Alumno('Diana', 41)
print(informacion.nombre)

# Práctica Herencia 2
# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: 
# edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.

class Mascota:

    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    
    print(f'La mascota es un Perro.')

datos = Perro(7, 'Luna', 4)
print(f'La mascota tiene {datos.cantidad_patas} patas, se llama {datos.nombre} y tiene {datos.edad} años.')


# Práctica Herencia 3
# Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los 
# métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.

class Vehiculo:

    def acelerar(self):
        print('Acelero')

    def frenar(self):
        print('Freno')

class Automovil(Vehiculo):
    print('Soy un automóvil que: ')

info = Automovil()
info.acelerar()
info.frenar()
>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
