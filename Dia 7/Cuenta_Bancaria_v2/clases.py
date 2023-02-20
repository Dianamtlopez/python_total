#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* NUEVO PLANTEAMIENTO: * JOSÉ LUIS CUENCA LAGUNA     *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos.
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a heredar de Persona.
class Cliente(Persona):

    def __init__(self, nombre, apellido, num_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    # Se muestren todos los datos del cliente, incluyendo el balance de su cuenta.
    def __str__(self):
        return (
            f"Señor(a): {self.nombre} {self.apellido} \nSaldo Actual: {self.balance}€"
        )

    # Un método llamado Depositar, que le va a permitir decidir cuánto dinero quiere agregar a su cuenta.
    def depositar(self, ingreso):
        self.balance += ingreso
        print(
            f"Su depósito de {ingreso}€, se ha registrado satisfactoriamente")

    # que le permita decidir cuánto dinero quiere sacar de su cuenta
    def retirar(self, retiro):
        if self.balance >= retiro:
            # Si tiene Fondos
            print(
                f"Su retiro de {retiro}€, se ha rigistrado satisfactoriamente")
            self.balance -= retiro
        else:
            # Si no tiene Fondos
            print("Saldo insuficiente!\n")