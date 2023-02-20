<<<<<<< HEAD
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar (self):
        print(f'{self.nombre} dice muuu')

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar (self):
        print(f'{self.nombre} dice beee')

mi_vaca = Vaca('Aurora')
mi_oveja = Oveja('Nube')

mi_vaca.hablar()
mi_oveja.hablar()

animales = [mi_vaca, mi_oveja]

for animal in animales:
    animal.hablar()

# Nota: en resumen, el polimorfismo obedece a clases diferentes 
# con metodos llamados igual, pero que cumplen funciones diferentes

def animal_habla(animales):
    animales.hablar()

# Clases distintas compartiendo el mosmo nombre del método o funcion
animal_habla(mi_vaca)
=======
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTODAD:             * UDEMY                       *
#******************************************************
class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar (self):
        print(f'{self.nombre} dice muuu')

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar (self):
        print(f'{self.nombre} dice beee')

mi_vaca = Vaca('Aurora')
mi_oveja = Oveja('Nube')

mi_vaca.hablar()
mi_oveja.hablar()

animales = [mi_vaca, mi_oveja]

for animal in animales:
    animal.hablar()

# Nota: en resumen, el polimorfismo obedece a clases diferentes 
# con metodos llamados igual, pero que cumplen funciones diferentes

def animal_habla(animales):
    animales.hablar()

# Clases distintas compartiendo el mosmo nombre del método o funcion
animal_habla(mi_vaca)
>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
animal_habla(mi_oveja)