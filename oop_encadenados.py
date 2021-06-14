# Asignatura: Métodos de encadenamiento
# Objetivos: Comprender cómo encadenar métodos
# En la última asignatura, su código podría haberse visto así:
# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(300)
# guido.make_withdrawal(50)
# guido.display_user_balance()
# Esto ocupa mucho espacio y estamos repitiendo nuestro llamado a guido muchas veces. Hay una manera de llamar a guido solo una vez y seguir adjuntando nuevas llamadas de método al final de la anterior, así:
# guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
# Esto se llama encadenamiento . Para que esto funcione, cada método debe devolver self . Al devolver self, si recordamos cómo funcionan las funciones, cada llamada al método ahora será igual a la instancia que la llamó.
# Por ejemplo, si guido.make_deposit(100)devuelve su propia instancia ( guido ), entonces podemos llamar a uno de los métodos de esa instancia después de esa llamada, como guido.make_deposit(100).make_withdrawal(50).
# class User:
#     def make_deposit(self, amount):
#         # aquí va tu código...
#         return self
# La práctica de hacer que POO devuelva su propia instancia es bastante común y se realiza en otros lenguajes de programación, aunque el nombre de la variable en algunos lenguajes no lo es self, sino en su lugar  this.
#     Actualiza tu asignación anterior para que los métodos de cada instancia estén encadenados	

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"Usuario: {self.name}, Saldo: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
charly = User("Charles Chaplin", "cchapliny@python.com")
guido.make_deposit(100000).make_deposit(150000).make_deposit(45000).make_withdrawal(12500).display_user_balance()
monty.make_deposit(360000).make_deposit(22800).make_withdrawal(12520).display_user_balance()
charly.make_deposit(850000).make_withdrawal(100000).make_withdrawal(50000).make_withdrawal(20000).display_user_balance()

print("Transferencia de 55000 de Guido a Charly")
guido.transfer_money(charly, 55000)

guido.display_user_balance()
charly.display_user_balance()