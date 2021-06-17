# Asignatura: BankAccount
# Objetivos : Practica clases de escritura
# A medida que continuamos pensando en nuestra aplicación bancaria, nos damos cuenta de que sería más preciso asignar un saldo no al
# usuario directamente, sino que en el mundo real, los usuarios tienen cuentas y las cuentas tienen saldos. ¡Esto nos da la idea de 
# que tal vez una cuenta es su propia clase ! Pero como dijimos, no es completamente independiente de una clase; las cuentas solo
# existen porque los usuarios las abren.
# Para esta tarea, no se preocupe por incluir información del usuario en la clase BankAccount. ¡Nos encargaremos de eso en la próxima lección!
# Primero, practiquemos más clases de escritura escribiendo una nueva clase de BankAccount . En la próxima lección, vincularemos 
# nuestras clases de usuario y cuenta bancaria.
# La clase BankAccount debe tener un saldo. Cuando se crea una nueva instancia de BankAccount, si se proporciona un monto, el saldo 
# de la cuenta debe establecerse inicialmente en ese monto; de lo contrario, el saldo debe comenzar en $ 0. La cuenta también debe 
# tener una tasa de interés, guardada como un decimal (es decir, el 1% se guardaría como 0.01), que debe proporcionarse cuando se 
# instancia. (Sugerencia: cuando se usan valores predeterminados en los parámetros, ¡el orden de los parámetros es importante!)
# La clase también debe tener los siguientes métodos:
#     deposit(self, cantidad) : aumenta el saldo de la cuenta en la cantidad dada
#     withdraw(self, cantidad) : disminuye el saldo de la cuenta en la cantidad dada si hay fondos suficientes; si no hay suficiente dinero, imprima un mensaje "Fondos insuficientes: cobrar una tarifa de $ 5" y deduzca $ 5
#     display_account_info(self) - imprime en la consola: ej. "Saldo: $ 100"
#     yield_interest(self) : aumenta el saldo de la cuenta en el saldo actual * la tasa de interés (siempre que el saldo sea positivo)

# Esto significa que necesitamos una clase que se vea así:
# class BankAccount:
# 	def __init__(self, int_rate, balance): # ¡No olvides agregar valores predeterminados para estos parámetros!
# 		 # su código aquí! (recuerde, aquí es donde especificamos los atributos para nuestra clase)
#        # no se preocupe por la información del usuario aquí; pronto involucraremos a la clase de usuario
# 	def deposit(self, amount):
# 	def withdraw(self, amount):
# 	def display_account_info(self):
# 	def yield_interest(self):

#     Crea una clase de BankAccount con los atributos tasa de interés y saldo	
#     Agrega un método de depósito a la clase BankAccount	
#     Agrega un método de retiro a la clase BankAccount	
#     Agrega un método display_account_info a la clase BankAccount	
#     Agrega un método yield_interest a la clase BankAccount	
#     Crea 2 cuentas	
#     En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)	
#     En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)

class BankAccount:
    def __init__(self, interes=0.01, saldo=0):
        self.interes = interes
        self.saldo = saldo

    def deposito(self, amount):
        self.saldo += amount
        return self

    def retiro(self, amount):
        self.saldo -= amount
        return self

    def display_account_info(self):
        print(f"Saldo: {self.saldo}")
        return self

    def calcula_interes(self):
        self.saldo += self.saldo * self.interes
        return self

guido = BankAccount(0.01, 100000)
monty = BankAccount(0.02, 200000)

guido.deposito(100000).deposito(100000).deposito(50000).retiro(50000).calcula_interes().display_account_info()
monty.deposito(200000).deposito(200000).retiro(25000).retiro(25000).retiro(25000).retiro(25000).calcula_interes().display_account_info()