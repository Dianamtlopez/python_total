#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
# Recuerda importar Path del módulo pathlib, y utilizar el método home()

from pathlib import Path

ruta_base = Path(Path.home())
print(ruta_base)

# Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" 
# a partir de la siguiente estructura de carpetas:
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
# Ruta Relativa
ruta = Path("Curso Python", "Día 6", "practicas_path.py")

# Práctica Path 3
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" 
# a partir de la siguiente estructura de carpetas:
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar 
# el objeto Path que refiere a la carpeta base del usuario.
# Ruta absoluta
ruta = Path(Path.home(), "Curso Python", "Día 6", "practicas_path.py")