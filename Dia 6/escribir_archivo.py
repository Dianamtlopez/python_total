#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# para escribir en el archivo, hay dos formas si le coloco w, el archivo es reemplazado por el nuevo texto
# y si no existe, solo se va a crear
archivo = open('prueba1.txt','w')
# para escribir saltos de linea
archivo.write('holan Mundo\n')
archivo.write('soy el nuevo texto\n')
# Otra manera de escribir es:
archivo.write("""Hola
mundo
aquí
estoy
""")
# Escribe los Strings y las concatenas juntas
archivo.writelines(['Hola', 'Mundo', 'Aquí', 'Estoy'])
# loop for pero no es un método muy práctico
lista = ['Hola', 'Mundo', 'Aquí', 'Estoy']
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

# abre el archivo, lleva el cursor hasta el final de lo que contenga y alli empieza a escribir.
archivo = open('prueba.txt', 'a')
archivo.write('Bienvenido\n')
archivo.close()

