<<<<<<< HEAD
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
from os import system
# Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos.
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a heredar de Persona.
class Cliente(Persona):
    def __init__(self,nombre, apellido, num_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    # Se muestren todos los datos del cliente, incluyendo el balance de su cuenta.
    def __str__(self):
        return (f"Señor(a): {self.nombre} {self.apellido} \nSaldo Actual: {self.balance}€")

    # Un método llamado Depositar, que le va a permitir decidir cuánto dinero quiere agregar a su cuenta.
    def depositar(self, ingreso):
        self.balance += ingreso
        print(f"Su depósito de {ingreso}€, se ha registrado satisfactoriamente")
        
    # que le permita decidir cuánto dinero quiere sacar de su cuenta
    def retirar(self, retiro):
        if self.balance >= retiro:
            # Si tiene Fondos
            print(f"Su retiro de {retiro}€, se ha rigistrado satisfactoriamente")
            self.balance -= retiro
        else:
            # Si no tiene Fondos
            print("Saldo insuficiente!\n")

def menu():
    eleccion_menu = ''
    # verificamos que el ingreso sea un numero por mas que esté en un string
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range (1,5):
        system('cls')
        print('Elige una opción: ')
        print("""
        [1] - Depositar Dinero
        [2] - Retirar Dinero
        [3] - Consultar Saldo
        [4] - Salir del programa
        """)
        eleccion_menu = input()
    return eleccion_menu

def crear_cliente():        
    system('cls')
    nombre = input("Digite su nombre: \t")
    nombre = nombre.upper()
    apellido = input("Digite sus apellidos: \t")
    apellido = apellido.upper()
    num_cuenta = []
    while len(num_cuenta) != 4:
        num_cuenta = input("Digite los ultimos 4 digitos de su cuenta: ")
    cliente = Cliente(nombre, apellido, num_cuenta)
    return cliente

def main():
    mi_cliente = crear_cliente()
    cont = ""
    while cont != 's':     
        eleccion_menu = menu()
        system('cls')
        match eleccion_menu:
            case '1':
                print("*****************************************************************\n")
                print(mi_cliente)
                print("\n*****************************************************************\n")
                ingresar_dinero = int(input("Digite el valor a depositar en cifra cerrada: "))
                mi_cliente.depositar(ingresar_dinero)
                print(f"Su nuevo saldo es: {mi_cliente.balance}€\n")
            case '2':
                print("*****************************************************************\n")
                print(mi_cliente)
                print("\n*****************************************************************\n")
                retirar_dinero = int(input("Digite el valor a retirar en cifra cerrada: "))
                mi_cliente.retirar(retirar_dinero)
                print(f"Su nuevo saldo es: {mi_cliente.balance}€\n")
            case '3':
                print("*****************************************************************\n")
                print(mi_cliente)
                print("\n*****************************************************************\n")
                print(f"El saldo total de su cuenta es: {mi_cliente.balance}€\n")
            case '4':
                print("Usted ha salido del sistema...")
                quit()
        
        input("Presione Enter para continuar...")

=======
#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTODAD:             * UDEMY                       *
#******************************************************
from os import system
# Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos.
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a heredar de Persona.
class Cliente(Persona):
    def __init__(self,nombre, apellido, num_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    # Se muestren todos los datos del cliente, incluyendo el balance de su cuenta.
    def __str__(self):
        return (f"Señor(a): {self.nombre} {self.apellido} \nSaldo Actual: {self.balance}€")

    # Un método llamado Depositar, que le va a permitir decidir cuánto dinero quiere agregar a su cuenta.
    def depositar(self, ingreso):
        self.balance += ingreso
        print(f"Su depósito de {ingreso}€, se ha registrado satisfactoriamente")
        
    # que le permita decidir cuánto dinero quiere sacar de su cuenta
    def retirar(self, retiro):
        if self.balance >= retiro:
            # Si tiene Fondos
            print(f"Su retiro de {retiro}€, se ha rigistrado satisfactoriamente")
            self.balance -= retiro
        else:
            # Si no tiene Fondos
            print("Saldo insuficiente!\n")

def menu():
    eleccion_menu = ''
    # verificamos que el ingreso sea un numero por mas que esté en un string
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range (1,5):
        system('cls')
        print('Elige una opción: ')
        print("""
        [1] - Depositar Dinero
        [2] - Retirar Dinero
        [3] - Consultar Saldo
        [4] - Salir del programa
        """)
        eleccion_menu = input()
    return eleccion_menu

def crear_cliente():        
    system('cls')
    nombre = input("Digite su nombre: \t")
    nombre = nombre.upper()
    apellido = input("Digite sus apellidos: \t")
    apellido = apellido.upper()
    num_cuenta = []
    while len(num_cuenta) != 4:
        num_cuenta = input("Digite los ultimos 4 digitos de su cuenta: ")
    cliente = Cliente(nombre, apellido, num_cuenta)
    return cliente

def main():
    mi_cliente = crear_cliente()
    cont = ""
    while cont != 's':     
        eleccion_menu = menu()
        system('cls')
        match eleccion_menu:
            case '1':
                print("*****************************************************************\n")
                print(mi_cliente)
                print("\n*****************************************************************\n")
                ingresar_dinero = int(input("Digite el valor a depositar en cifra cerrada: "))
                mi_cliente.depositar(ingresar_dinero)
                print(f"Su nuevo saldo es: {mi_cliente.balance}€\n")
            case '2':
                print("*****************************************************************\n")
                print(mi_cliente)
                print("\n*****************************************************************\n")
                retirar_dinero = int(input("Digite el valor a retirar en cifra cerrada: "))
                mi_cliente.retirar(retirar_dinero)
                print(f"Su nuevo saldo es: {mi_cliente.balance}€\n")
            case '3':
                print("*****************************************************************\n")
                print(mi_cliente)
                print("\n*****************************************************************\n")
                print(f"El saldo total de su cuenta es: {mi_cliente.balance}€\n")
            case '4':
                print("Usted ha salido del sistema...")
                quit()
        
        input("Presione Enter para continuar...")

>>>>>>> e81551edba0bfe8ec6814b4d652101e358628718
main()