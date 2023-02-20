<<<<<<< HEAD
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('Ja Ja Ja')

    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

# Orden en que se resuelve la herencia
print(Nieto.__mro__)

# Práctica Herencia Extendida 1
# Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, 
# y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita
# a esta clase heredar correctamente de Padre y Madre.
# Completa el código suministrado a continuación para lograrlo.

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre, Padre):
    pass
    

mi_hijo = Hija()
mi_hijo.reir()
mi_hijo.trabajar()

# Práctica Herencia Extendida 2
# "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; 
# y amamanta a sus crías pero no tienen mamas." (National Geographic)
# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, 
# tal que "construyas" un animal que tiene los siguientes métodos y atributos:
# - poner_huevos()
# - tiene_pico = True
# - vertebrado = True
# - venenoso = True
# - nadar()
# - caminar()
# - amamantar()

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez, Reptil, Ave, Mamifero):
    pass

mi_animal = Ornitorrinco()
print(mi_animal)

# Práctica Herencia Extendida 3
# Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. 
# Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método 
# hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"
# [1]: asegúrate de utilizar return seguido de una cadena de texto

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

mi_hijo = Hijo()
print(mi_hijo.hobby())

mi_padre = Padre()
=======
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('Ja Ja Ja')

    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

# Orden en que se resuelve la herencia
print(Nieto.__mro__)

# Práctica Herencia Extendida 1
# Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, 
# y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita
# a esta clase heredar correctamente de Padre y Madre.
# Completa el código suministrado a continuación para lograrlo.

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre, Padre):
    pass
    

mi_hijo = Hija()
mi_hijo.reir()
mi_hijo.trabajar()

# Práctica Herencia Extendida 2
# "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; 
# y amamanta a sus crías pero no tienen mamas." (National Geographic)
# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, 
# tal que "construyas" un animal que tiene los siguientes métodos y atributos:
# - poner_huevos()
# - tiene_pico = True
# - vertebrado = True
# - venenoso = True
# - nadar()
# - caminar()
# - amamantar()

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez, Reptil, Ave, Mamifero):
    pass

mi_animal = Ornitorrinco()
print(mi_animal)

# Práctica Herencia Extendida 3
# Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. 
# Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método 
# hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"
# [1]: asegúrate de utilizar return seguido de una cadena de texto

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

mi_hijo = Hijo()
print(mi_hijo.hobby())

mi_padre = Padre()
>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
print(mi_padre.hobby())