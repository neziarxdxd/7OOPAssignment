amount = 10_000.00
name = ""
transact= True
class Transact:
    
    def __init__(self,amount,name):
        self.amount = amount
        self.name= name

    def Withdraw(self, money):    
        

        
        if self.amount <= 0 or self.amount<money:
            print("No enough balance for your request",self.amount)
        else:
            self.amount=self.amount - money
            print("Thank you for your withdrawal. Your current amount is :",self.amount)
            
    def Deposit(self, money):
        self.amount=self.amount + money        
        print("Thank you for your withdrawal. Your current amount is :",self.amount)

    def DoYouHave(self):
        x= input("Do you have any transaction? [Y or y to continue] ")        
        return (x).lower() =="y"
    def TRANSX(self):
        choice = input("Choose transaction: [W]-withdraw [D]-deposit [E]-exit : ").lower()
        if choice == "w":
            withdraw_money = float(input("Enter the amount: "))
            a.Withdraw(withdraw_money)
            
            
        elif choice == "d":                
            deposit_money = float(input("Enter the amount: "))
            a.Deposit(deposit_money)
            
            
        elif choice == "e":
            exit()
            
        else:
            print("NO CHOICE")
            
transact= True
print("WELCOME!")
name = input("Enter your name: ")

a= Transact(amount,name)
print("Current Amount: ", amount)
while transact:    
    a.TRANSX()
    transact=a.DoYouHave()
    

print("Thank youuu",name,"! See us again")

    
    
    
    
    

