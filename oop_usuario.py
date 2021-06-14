# Asignatura: usuario
# Objetivos : Practica crear una clase y crear instancias a partir de ella
#             Practica el acceso a los métodos y atributos de diferentes instancias.
# Si has estado siguiendo, utilizará la clase de usuario que hemos estado discutiendo para esta tarea.
# Para esta tarea, agregaremos algunas funcionalidades a la clase Usuario:
#     make_withdrawal (self, amount) : haz que este método disminuya el saldo del usuario en la cantidad especificada
#     display_user_balance (self) : haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
#         p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
#     BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user
# 
#     Crea un archivo con la clase Usuario, incluidos los métodos __init__ y make_deposit
#     Agrega un método make_withdrawal a la clase Usuario	
#     Agrega un método display_user_balance a la clase Usuario	
#     Crea 3 instancias de la clase de usuario	
#     Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo	
#     Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo	
#     Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo	
#     BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y luego imprima los saldos de ambos usuarios.

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
    	self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"Usuario: {self.name}, Saldo: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
charly = User("Charles Chaplin", "cchapliny@python.com")
guido.make_deposit(100000)
guido.make_deposit(150000)
guido.make_deposit(45000)
guido.make_withdrawal(12500)
guido.display_user_balance()

monty.make_deposit(360000)
monty.make_deposit(22800)
monty.make_withdrawal(12520)
monty.display_user_balance()

charly.make_deposit(850000)
charly.make_withdrawal(100000)
charly.make_withdrawal(50000)
charly.make_withdrawal(20000)
charly.display_user_balance()

print("Transferencia de 55000 de Guido a Charly")
guido.transfer_money(charly, 55000)

guido.display_user_balance()
charly.display_user_balance()