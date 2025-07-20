from test import User

class Myuser(User):
    def __init__(self,bank_balance:int,name: str, email: str, user_type: str):

        super().__init__(name,email,user_type)

        self.var1=1
        self.var2=2
        self.bank_balance=bank_balance


    
myuser=Myuser("Satvik","abc@gmail.com","m")

print(myuser.logged_in)
