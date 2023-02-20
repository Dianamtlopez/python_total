#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
"""Diccionarios clave:valor"""

# Creacion del diccionario
diccionario = {"c1":"valor1","c2":"valor1"}
print(type(diccionario))
print(diccionario)

# para consultar informacion
resultado = diccionario["c1"]
print(resultado)

cliente = {"nombre":"Diana", "apellido":"Toro", "Peso":45.5, "talla":1.55}
consulta = (cliente["apellido"])
# para consultar
print(consulta)

# Diccionarios dentro de diccionarios
dic = {"c1":55, "c2":[10, 20, 30], "c3":{"s1":100, "s2":200}}
# imprimir lo que hay en la clave 2 indice 1
print(dic["c2"][1])

# imprimir el diccionario que está en diccionario
print(dic["c3"])

# imprimir el diccionario que está en diccionario clave 1
print(dic["c3"]["s1"])

dic1 = {"c1":['a','b','c'], "c2":['d','e','f']}

# imprimir la letra e en mayuscula
print((dic1["c2"][1]).upper())

# Agregar elementos a diccionarios
dic2 = {1:'a',2:'b'}
dic2[3] = 'c'
print(dic2[3])

# sobreescribir claves existentes
dic2[2] = 'B'
print(dic2)

# Imprimir todas las claves de un diccionario
print(dic2.keys())

# Conocer todos los valores
print(dic2.values())

# Imprimir todo el diccionario
print(dic2.items())

# Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente 
# diccionario.
# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se
# encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o 
# índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

# Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves 
# según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic[2] = 36
mi_dic[3] = "Editora"
mi_dic["pais"] = "Colombia"
print(mi_dic)

