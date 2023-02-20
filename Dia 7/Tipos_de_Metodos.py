<<<<<<< HEAD
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

    # Métodos de instancia porque afecta al self
    def piar(self):
        # Cada vez q se invoque un atributo, necesitamos relacionar a quien pertenece esste atributo
        print(f'Pio, mi color es {self.color}')
    
    # Métodos de instancia porque afecta al self
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros.')

    # Método de instancia, puede acceder y modificar los atributos del objeto
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')
        # Puede acceder a otros métodos
        self.piar()
    
    # Método de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos.')
        cls.alas = False
        # No se puede modificar atributos de instancia self
        # Si modifica atributos de clase
        print(Pajaro.alas)

    # Método estático, no se refieren ni a la clase ni a la instancia
    @staticmethod
    def mirar():
        # No pueden modificar el estado de una instancia ni los atributos de la clase
        print('El pajaro mira')


# instancia de la clase
piolin = Pajaro('Amarillo', 'canario')
piolin.piar()
piolin.volar(20)
piolin.pintar_negro()

# Puede modificar el estado de la clase
piolin.alas = False

print(piolin.alas)

# Llamada a metodos de clase y estos no necesitan instancia para ejecutarse
Pajaro.poner_huevos(3)

# Llamada a métodos estáticos
Pajaro.mirar()

# Práctica Tipos de Métodos 1
# Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla 
# "Inhalar... Exhalar"

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

# Práctica Tipos de Métodos 2
# Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, 
# estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.

class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(Jugador.vivo)

Jugador.revivir()
        
# Práctica Tipos de Métodos 3
# Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de 
# Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.

class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
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

    # Métodos de instancia porque afecta al self
    def piar(self):
        # Cada vez q se invoque un atributo, necesitamos relacionar a quien pertenece esste atributo
        print(f'Pio, mi color es {self.color}')
    
    # Métodos de instancia porque afecta al self
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros.')

    # Método de instancia, puede acceder y modificar los atributos del objeto
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')
        # Puede acceder a otros métodos
        self.piar()
    
    # Método de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos.')
        cls.alas = False
        # No se puede modificar atributos de instancia self
        # Si modifica atributos de clase
        print(Pajaro.alas)

    # Método estático, no se refieren ni a la clase ni a la instancia
    @staticmethod
    def mirar():
        # No pueden modificar el estado de una instancia ni los atributos de la clase
        print('El pajaro mira')


# instancia de la clase
piolin = Pajaro('Amarillo', 'canario')
piolin.piar()
piolin.volar(20)
piolin.pintar_negro()

# Puede modificar el estado de la clase
piolin.alas = False

print(piolin.alas)

# Llamada a metodos de clase y estos no necesitan instancia para ejecutarse
Pajaro.poner_huevos(3)

# Llamada a métodos estáticos
Pajaro.mirar()

# Práctica Tipos de Métodos 1
# Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla 
# "Inhalar... Exhalar"

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

# Práctica Tipos de Métodos 2
# Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, 
# estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.

class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(Jugador.vivo)

Jugador.revivir()
        
# Práctica Tipos de Métodos 3
# Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de 
# Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.

class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
