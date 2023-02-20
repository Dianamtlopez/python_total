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
        self.color = color
        self.especie = especie

    # Métodos de clase
    def piar(self):
        # Cada vez q se invoque un atributo, necesitamos relacionar a quien pertenece esste atributo
        print(f'Pio, mi color es {self.color}')
    
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros.')

# instancia de la clase
piolin = Pajaro('Amarillo', 'canario')

piolin.piar()
piolin.volar(50)

# Práctica Métodos 1
# Crea una clase Perro. Dicho perro debe poder ladrar.
# Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".

class Perro:

    def ladrar(self):
        print("Guau!")

ladra = Perro()
ladra.ladrar()

# Práctica Métodos 2
# Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
# Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

# Práctica Métodos 3
# Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje
# "La alarma ha sido pospuesta {cantidad_minutos} minutos"

class Alarma:

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

resultado = Alarma()
=======
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
        self.color = color
        self.especie = especie

    # Métodos de clase
    def piar(self):
        # Cada vez q se invoque un atributo, necesitamos relacionar a quien pertenece esste atributo
        print(f'Pio, mi color es {self.color}')
    
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros.')

# instancia de la clase
piolin = Pajaro('Amarillo', 'canario')

piolin.piar()
piolin.volar(50)

# Práctica Métodos 1
# Crea una clase Perro. Dicho perro debe poder ladrar.
# Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".

class Perro:

    def ladrar(self):
        print("Guau!")

ladra = Perro()
ladra.ladrar()

# Práctica Métodos 2
# Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
# Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

# Práctica Métodos 3
# Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje
# "La alarma ha sido pospuesta {cantidad_minutos} minutos"

class Alarma:

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

resultado = Alarma()
>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
resultado.postergar(20)