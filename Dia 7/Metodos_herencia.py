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

    def hablar(self):
        print("Este animal emite un sonido")

# Hereda de la clase animal, 
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        """
        # una forma
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo
        """
        # Otra Forma
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo


    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros}, metros')

# Instancia de clase Animal
mi_animal = Animal(5, 'negro')
# métodos de clase padre
mi_animal.nacer()
mi_animal.hablar()

# Las clases hijas pueden tener 3 típos de métodos
# los propios, los heredados y los modificados
# instancia de clase hija Pajaro con atributos heredados y propios
# Métodos modificados
piolin = Pajaro(2, 'Amarillo', 60)
# métodos propios de clase hija
piolin.hablar()
piolin.volar(100)


# piolin ha heredado de la clase padre
piolin.nacer()
piolin.hablar()


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

    def hablar(self):
        print("Este animal emite un sonido")

# Hereda de la clase animal, 
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        """
        # una forma
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo
        """
        # Otra Forma
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo


    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros}, metros')

# Instancia de clase Animal
mi_animal = Animal(5, 'negro')
# métodos de clase padre
mi_animal.nacer()
mi_animal.hablar()

# Las clases hijas pueden tener 3 típos de métodos
# los propios, los heredados y los modificados
# instancia de clase hija Pajaro con atributos heredados y propios
# Métodos modificados
piolin = Pajaro(2, 'Amarillo', 60)
# métodos propios de clase hija
piolin.hablar()
piolin.volar(100)


# piolin ha heredado de la clase padre
piolin.nacer()
piolin.hablar()


>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
