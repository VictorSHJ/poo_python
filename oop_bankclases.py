# Asignatura: usuarios con cuentas bancarias
# Objetivos: Practica clases de escritura con asociaciones
# Actualiza tu clase de usuario existente para tener una asociación con la clase BankAccount. No deberías tener que cambiar nada en la clase BankAccount. Las firmas de método de la clase Usuario (la primera línea del método con la palabra clavedef) también deben permanecer iguales.
# Por ejemplo, nuestra clase de usuario actualmente tiene un método como este:
# class User:
#     def user_deposito(self, amount):
#     	self.saldo += amount	# hmmm ... la clase de usuario ya no tiene un atributo account_balance
# Pero nuestra clase de usuario ya no tiene un atributo self.saldo. En cambio, hemos reemplazado esto con una instancia 
# de BankAccount con el nombre de self.cuenta. ¡Eso significa que nuestro user_deposito (y otros métodos que hacen referencia a 
# self.saldo) deben actualizarse! Ese es el objetivo de esta tarea.
# Recuerda que en nuestros métodos de usuario, ahora podemos acceder a la clase BankAccount a través de nuestro atributo self.cuenta, así:
# class User:
#     def example_method(self):
#         self.deposito(100)		# podemos llamar los métodos de la instancia BankAccount 
#         print(self.saldo)	   	    # o acceder a sus atributos

#  Actualiza el metodo __init__ de la clase User
#  Actualiza el metodo user__deposito de la clase User	
#  Actualiza el metodo make_withdrawal de la clase User	
#  Actualiza el metodo display_user_balance de la clase User	
#     SENSEI BONUS: Permite al usuario tener varias cuentas; actualiza los metodos para que el usuario pueda especificar de cual 
#     cuenta ellos quieren depositar o retirar	
#     BONUS 2: Modificar la función "transfer_money" de la clase User	

class User:
    def __init__(self, username, email_address):
        self.name   = username
        self.email  = email_address
        self.cuenta = BankAccount(interes=0.02, saldo=0)	
    def user_deposito(self, amount):
        self.saldo = self.cuenta.deposito(amount)
        return self
    def user_retiro(self, amount):
        self.saldo = self.cuenta.retiro(amount)
        return self
    def user_disp_balance(self):
        print(f"Usuario: {self.name}, Saldo: {self.cuenta.display_saldo()}")
        return self
    def transferencia(self, other_user, amount):
        self.user_retiro(amount)
        other_user.user_deposito(amount)
    def __str__(self):        
        return (f"Nombre : {self.name}, Correo: {self.email}, {self.cuenta}")
    
class BankAccount:
    def __init__(self, interes=0, saldo=0):
        self.interes = interes
        self.saldo = saldo

    def deposito(self, amount):
        self.saldo += amount
        return self

    def retiro(self, amount):
        self.saldo -= amount
        return self

    def display_saldo(self):
        # print(f"Saldo: {self.saldo}")
        return self.saldo

    def calcula_interes(self):
        self.saldo += self.saldo * self.interes
        return self

    def __str__(self):        
        return (f"Interes : {self.interes}, Saldo: {self.saldo}")

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

print(guido)
print(monty)

guido.user_deposito(1000)
monty.user_deposito(850)
print("Deposito 1000:", guido)
guido.user_retiro(400)
print("Retiro 400:", guido)

guido.user_disp_balance()
monty.user_disp_balance()

# Transferir de guido a monty 270

guido.transferencia(monty, 270)
print("Transferir de guido a monty 270")
guido.user_disp_balance()
monty.user_disp_balance()


