#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
if 10 > 9:
    print('Es correcto')

x = True
if x:
    print('Es correcto')

if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')

mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No sé qué animal tienes')

edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No Aprobado')
else:
    print('Eres adulto')

habla_ingles = True
sabe_python = False
if sabe_python and habla_ingles:
    print("Cumples con los requisitos para postularte")
elif sabe_python and habla_ingles:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif sabe_python and not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif not sabe_python and habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
