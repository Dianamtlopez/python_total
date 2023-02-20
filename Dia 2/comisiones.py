#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""Segundo proyecto"""

nombre = input("Ingrese su nombre: ")
ventas = int(input("Ingrese el valore de sus ventas este mes: "))
comision = round((ventas * 13 / 100),2)
print(f"Hola {nombre}, este mes usted vendió {ventas} y su comision de este mes es: ${comision}")