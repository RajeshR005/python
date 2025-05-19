#practice questions
#Create account class with 2 attributes Balance, account No
# Create a methods for debit, credit and printing the balance


import json  
class bank:
    account_balance={}
    def __init__(self,accountno):
        self.acc=accountno
        
        with open("py practice\\functions\\current_balance.json") as f:
            self.data1=json.load(f)
            self.balance=self.data1[0]["balance"]
            
    def credit(self,amount):
        self.balance=self.balance+amount
        self.data1[0]["balance"]=self.balance
        print(f"₹{amount} was credit in your account")
        
     
        with open("py practice\\functions\\current_balance.json",'w') as f:
            json.dump(self.data1,f,indent=3)
        print(f"Available Balance ₹{self.balance}")
            
    def debit(self,amount):
        self.balance=self.balance-amount
        self.data1[0]["balance"]=self.balance
        print(f"₹{amount} was Debited from your account")
        with open("py practice\\functions\\current_balance.json",'w') as f:
            json.dump(self.data1,f,indent=3)
        print(f"Available Balance ₹{self.balance}")
    # @staticmethod 
    def balance1(self):
        bal=str(self.balance)
        print(f"Available Balance ₹{bal}")
bank1=bank(30072002)
user_preference=int(input("credit=1\ndebit=2\nbalance=3"))
if user_preference==1:
    amount=int(input("Enter the amount for Credit"))
    bank1.credit(amount)
elif user_preference==2:
    amount=int(input("Enter the amount for Debit"))
    bank1.debit(amount)
elif user_preference==3:
    bank1.balance1()
else:
    print("Enter your correct Choice")


        