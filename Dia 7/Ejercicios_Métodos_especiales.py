<<<<<<< HEAD
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Práctica Métodos Especiales 1
# Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima 
# el objeto, devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre 
# comillas dobles).

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

mi_libro = Libro('Cien Años de Soledad', 'Gabriel García Marquez', 200)

print(mi_libro)

# Práctica Métodos Especiales 2
# Dada la clase Libro, implementa el método especial __len__ para que cada vez 
# que se ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

mi_libro = Libro('Cien Años de Soledad', 'Gabriel García Marquez', 200)

print(len(mi_libro))
print(mi_libro)

# Práctica Métodos Especiales 3
# Dada la clase Libro, implementa el método especial __del__ para que el usuario 
# sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez 
# que el libro se elimine.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        # Además de eliminar  coloque el dato que este método designe
        print('Se ha eliminado el Libro')

mi_libro = Libro('Cien Años de Soledad', 'Gabriel García Marquez', 200)

=======
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTODAD:             * UDEMY                       *
#******************************************************
# Práctica Métodos Especiales 1
# Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima 
# el objeto, devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre 
# comillas dobles).

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

mi_libro = Libro('Cien Años de Soledad', 'Gabriel García Marquez', 200)

print(mi_libro)

# Práctica Métodos Especiales 2
# Dada la clase Libro, implementa el método especial __len__ para que cada vez 
# que se ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

mi_libro = Libro('Cien Años de Soledad', 'Gabriel García Marquez', 200)

print(len(mi_libro))
print(mi_libro)

# Práctica Métodos Especiales 3
# Dada la clase Libro, implementa el método especial __del__ para que el usuario 
# sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez 
# que el libro se elimine.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        # Además de eliminar  coloque el dato que este método designe
        print('Se ha eliminado el Libro')

mi_libro = Libro('Cien Años de Soledad', 'Gabriel García Marquez', 200)

>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
del mi_libro