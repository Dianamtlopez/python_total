#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

# capturar datos del tiempo
import datetime

mi_hora = datetime.time(17, 35)
# Ver el tipo de datos
print(type(mi_hora))
print(mi_hora)
print(mi_hora.hour)
print(mi_hora.minute)
print(mi_hora.second)

# También podemos trabajar con fechas
mi_dia = datetime.date(2025, 10, 17)
# Ver el tipo de datos
print(type(mi_dia))
print(mi_dia)
print(mi_dia.day)
print(mi_dia.month)
print(mi_dia.year)

# Otro formato de fecha
print(mi_dia.ctime())
print(mi_dia.today())

# importar frcha y hora
from datetime import datetime
mi_fecha1 = datetime(2025, 5 , 15, 22, 10, 15, 2500)
print(mi_fecha1)

# Cambiar datos
mi_fecha1 = mi_fecha1.replace(month = 11)
print(mi_fecha1)

# Calcular tiempos entre uno y otro
from datetime import date
nacimiento = date(1956, 2, 27)
defuncion = date(2002, 1, 13)

vida = defuncion - nacimiento
print(vida.days)

# importar frcha y hora
from datetime import datetime
despierta = datetime(2024 , 10 , 17, 10, 30)
duerme = datetime(2024, 10, 18, 1, 30)

vigilia = duerme - despierta
print(vigilia)
print(vigilia.seconds)

################################################################################
# Práctica Módulo Datetime 1
# Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999

# capturar datos del tiempo
import datetime

mi_fecha = datetime.date(1999, 2, 3)

# Práctica Módulo Datetime 2
# Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.

# capturar datos del tiempo
import datetime

hoy = datetime.date.today()
print(hoy)

# Práctica Módulo Datetime 3
# En una variable llamada minutos, almacena únicamente los minutos de la hora actual.
# Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe 
# almacenar el valor 43

# importar frcha y hora
import datetime

# Obtener la hora actual
hora_actual = datetime.datetime.now()
# Obtener los minutos de la hora actual
minutos = hora_actual.minute
print(minutos)