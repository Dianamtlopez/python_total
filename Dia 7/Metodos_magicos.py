<<<<<<< HEAD
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTODAD:             * UDEMY                       *
#******************************************************
# Métodos especiales, dundero standard, son métodos que se forman por doble guón bajo al inicio y al final de sus nombres
# __init__ se usa para iniciar atributos de una clase nueva
# __mro__ para conocer el orden en el que se organiza la busqueda de metodos generados
# __bases__ La tupla de clases base de las que deriva una clase
# __subclases__ Retorna una lista de todas las referencias de subclases que todavía estén vivas

# hay muchos métodos más que son empleados para crear funcionalidades que no pueden ser 
# representados en un método regular

# Ejemplo de clases
mi_lista = [1,1,1,1,1,1,1,1]
print(len(mi_lista))

# Creo una clase
class Objeto:
    pass

# creo una instancia del objeto
mi_objeto = Objeto()
# Representacion en un string de esa instancia de la  Objeto
print(mi_objeto)

# Cuando yo deseo usar las funciones básicas de python como len print y otreas en mis propios objetos
# aqui entran en acción los métodos especiales 
class CD:
    # definir atributos
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    def __str__(self):
        # Me ayuda a definir la forma de como qqueremos que se manifieste un string de mi clase
        # cada vez que un método lo solicite
        return f"Album: {self.titulo} de {self.autor}"
        # esto es lo que quiero que devuelva en formato string, cada vez que solicite algún método

    def __len__(self):
        # cuando invoque el método len(), quiero que me devuelva la cantidad de canciones
        return self.canciones

    def __del__(self):
        # Además de eliminar  coloque el dato que este método designe
        print('Se ha eliminado el cd')

mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)
print(len(mi_cd))

=======
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Métodos especiales, dundero standard, son métodos que se forman por doble guón bajo al inicio y al final de sus nombres
# __init__ se usa para iniciar atributos de una clase nueva
# __mro__ para conocer el orden en el que se organiza la busqueda de metodos generados
# __bases__ La tupla de clases base de las que deriva una clase
# __subclases__ Retorna una lista de todas las referencias de subclases que todavía estén vivas

# hay muchos métodos más que son empleados para crear funcionalidades que no pueden ser 
# representados en un método regular

# Ejemplo de clases
mi_lista = [1,1,1,1,1,1,1,1]
print(len(mi_lista))

# Creo una clase
class Objeto:
    pass

# creo una instancia del objeto
mi_objeto = Objeto()
# Representacion en un string de esa instancia de la  Objeto
print(mi_objeto)

# Cuando yo deseo usar las funciones básicas de python como len print y otreas en mis propios objetos
# aqui entran en acción los métodos especiales 
class CD:
    # definir atributos
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    def __str__(self):
        # Me ayuda a definir la forma de como qqueremos que se manifieste un string de mi clase
        # cada vez que un método lo solicite
        return f"Album: {self.titulo} de {self.autor}"
        # esto es lo que quiero que devuelva en formato string, cada vez que solicite algún método

    def __len__(self):
        # cuando invoque el método len(), quiero que me devuelva la cantidad de canciones
        return self.canciones

    def __del__(self):
        # Además de eliminar  coloque el dato que este método designe
        print('Se ha eliminado el cd')

mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)
print(len(mi_cd))

>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
del mi_cd