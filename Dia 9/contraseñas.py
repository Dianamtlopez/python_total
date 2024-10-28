#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

def calcular_contraseñas_posibles(n):
    # Suponemos que n es el número de opciones para cada dígito
    contraseñas_posibles = n**3
    return contraseñas_posibles

# Ejemplo: si cada dígito puede ser un número del 0 al 9 (10 opciones),
# entonces el número de contraseñas posibles sería 10^3 = 1000.
opciones_por_dígito = 10
contraseñas_posibles = calcular_contraseñas_posibles(opciones_por_dígito)
print(f"El número de contraseñas posibles es: {contraseñas_posibles}")


print(10**3)

tamaño_disco = 16 * 1024 * 1024 * 1024  # Convertimos de GB a bytes
tamaño_sector = 512  # Tamaño de un sector en bytes

sector_cantidad = tamaño_disco // tamaño_sector

print(sector_cantidad)