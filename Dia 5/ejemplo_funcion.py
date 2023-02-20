#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
precios_cafe =[("Capuchino",1.5),("Expleso", 1.2),("Moka",1.9)] 
for elemento in precios_cafe:
    print(elemento)

# Desempaco la tupla y elijo un elemento
for cafe, precio in precios_cafe:
    print(cafe)
    
# costo de cada café
for cafe, precio in precios_cafe:
    print(precio *0.45)

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ""

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass
    return cafe_caro, precio_mayor
# asigna a las dos variables, su valor correspondiente
cafe, precio = (cafe_mas_caro(precios_cafe))
print(f"El café mas caro es {cafe}, cuyo precio es {precio}")

