#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# crear o mover archivos
# enumerar archivos
# crear rutas basadas en strings

from pathlib import Path

# Construye objetos que se comporta como rutas de acceso, en este caso tiene una ruta relativa, 
# que puede estar en algun lado
guia = Path("Barcelona", "Sagrada_pamilia")
print(guia)

# Devuelve una instancia al directorio Path con una ruta absoluta al directorio Path
base = Path.home()
print(base)
# Tengo la ruta relativa
guia = Path("Barcelona", "Sagrada_pamilia.txt")
print(guia)

# Si uno estos dos, se crea una ruta absoluta que va hasta el archivo sagrada_familia
guia = Path(base, "Barcelona", "Sagrada_pamilia.txt")
print(guia)

# Nota: el constructor Path acepta tanto cadenas como objetos de Path
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_pamilia.txt"))
print(guia)

# cosntruimos una segunda ruta con otro nombre de archivos
guia2 = guia.with_name("La_Pedrera.txt")
print(guia2)

# Recorrer el arbol de ancestros de un rachivo
print(guia.parent)
print(guia.parent.parent)

# Creo un historial de carpetas y archivos:
guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob('*.txt'):
    print(txt)

# Esto hace que se incluyan carpetas y sub carpetas y enumere todos los txt que encuentre
for txt in Path(guia).glob('**/*.txt'):
    print(txt)

# Calcular rutas relacionadas entre si
guia = Path("Europa", "España", "Barcelona", "Sagrada Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
# que arranque desde Europa hacia abajo
print(en_europa)
# Que se genere desde Europa y España hacia abajo
print(en_espania)
