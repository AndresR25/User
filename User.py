class User:
    def __init__(self,n,lt,ag):
        self.name=n
        self.lastname=lt
        self.age=ag
        self.amount=0

    def deposit(self, amount):
        self.amount += amount
    
    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()



Andres=User("Andres","Rodriguez",19)
Silvia=User("Silvia","Alfaro",40)
Emilce=User("Emilce","Castillo",70)

Andres.deposit(5000)
Andres.deposit(10000)
Andres.deposit(15000)
Andres.make_withdrawl(1000)
Andres.display_user_balance()


Silvia.deposit(1000)
Silvia.deposit(2000)
Silvia.make_withdrawl(500)
Silvia.make_withdrawl(1000)
Silvia.display_user_balance()

Emilce.deposit(2000)
Emilce.make_withdrawl(1000)
Emilce.make_withdrawl(500)
Emilce.make_withdrawl(2000)
Emilce.display_user_balance()

Andres.transfer_money(1000,Emilce)