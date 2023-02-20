<<<<<<< HEAD
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* NUEVO PLANTEAMIENTO: * JOSÉ LUIS CUENCA LAGUNA     *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************

from funciones import crear_cliente, encabezado, limpia_pantalla, menu


def main():

    mi_cliente = crear_cliente()

    while True:     
        eleccion_menu = menu()
        limpia_pantalla()
        match eleccion_menu:
            case '1':
                encabezado(mi_cliente)
                ingresar_dinero = int(input("Digite el valor a depositar en cifra cerrada: "))
                mi_cliente.depositar(ingresar_dinero)
                print(f"Su nuevo saldo es: {mi_cliente.balance}€\n")
            case '2':
                encabezado(mi_cliente)
                retirar_dinero = int(input("Digite el valor a retirar en cifra cerrada: "))
                mi_cliente.retirar(retirar_dinero)
                print(f"Su nuevo saldo es: {mi_cliente.balance}€\n")
            case '3':
                encabezado(mi_cliente)
                print(f"El saldo total de su cuenta es: {mi_cliente.balance}€\n")
            case '4':
                print("Usted ha salido del sistema...")
                quit()
        
        input("Presione Enter para continuar...")

=======
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* NUEVO PLANTEAMIENTO: * JOSÉ LUIS CUENCA LAGUNA     *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTODAD:             * UDEMY                       *
#******************************************************

from funciones import crear_cliente, encabezado, limpia_pantalla, menu


def main():

    mi_cliente = crear_cliente()

    while True:     
        eleccion_menu = menu()
        limpia_pantalla()
        match eleccion_menu:
            case '1':
                encabezado(mi_cliente)
                ingresar_dinero = int(input("Digite el valor a depositar en cifra cerrada: "))
                mi_cliente.depositar(ingresar_dinero)
                print(f"Su nuevo saldo es: {mi_cliente.balance}€\n")
            case '2':
                encabezado(mi_cliente)
                retirar_dinero = int(input("Digite el valor a retirar en cifra cerrada: "))
                mi_cliente.retirar(retirar_dinero)
                print(f"Su nuevo saldo es: {mi_cliente.balance}€\n")
            case '3':
                encabezado(mi_cliente)
                print(f"El saldo total de su cuenta es: {mi_cliente.balance}€\n")
            case '4':
                print("Usted ha salido del sistema...")
                quit()
        
        input("Presione Enter para continuar...")

>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
main()