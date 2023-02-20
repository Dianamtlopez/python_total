#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
def reemplazar(lista):
    # Recibo la lista y la ino por medio de espacios para que me quede en forma de texto para poder
    # manipular los string
    lista_minuscula = " ".join(lista)
    # convierto el texto a minuscula
    lista_minuscula = lista_minuscula.lower()
    # vuelvo nuevamente el texto a lista para poder convertir cada palabra en iterable
    lista_minuscula = lista_minuscula.split()
    # creo la nueva lista vacía para almacenar cada palabra
    new_list = []
    # Inicializo la variable texto para almacenar cada palabra sin tildes
    texto = ''
    for palabra in lista_minuscula:
        # a la variable texto le asigno cada palabra en forma de string para manipularla
        texto = str(palabra)
        # inicio el reemplazo de las tildes en cada palabra
        texto = texto.replace('á','a')
        texto = texto.replace('é','e')
        texto = texto.replace('í','i')
        texto = texto.replace('ó','o')
        texto = texto.replace('ú','ú')
        texto = texto.replace('ü','u')
        # Agrego cada palabra a la nueva lista
        new_list.append(texto)
    # Retorno la lista
    return new_list
    
# Lista inicial           
lista = ['Adaptación', 'Agudo', 'Antibiótico', 'Artritis', 'Ataxia', 'Atrofia', 'Circulación', 'Cirugía', 'Conducta', 'Contractura', 'Crónico', 'Cuadriplejia', 'Diagnóstico']
resultado = reemplazar(lista)
print(resultado)

