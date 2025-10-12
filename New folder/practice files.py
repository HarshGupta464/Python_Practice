class Account:
    def __init__ (self, bal, accno):
        self.bal=bal
        self.accno=accno
    
    def debit(self,amnt):
        self.bal -= amnt
        print("Rs", amnt, "was debited")
        print("Balance = ",self.balance())
        
    def credit(self,amnt):
        self.bal += amnt
        print("Rs", amnt, "was credited")
        print("Balance = ",self.balance())
        
    def balance(self):
        return self.bal
        
acc1=Account(80000, 933508)
print(acc1.bal)
print(acc1.accno)
acc1.credit(7000)
acc1.debit(400)
acc1.debit(3000)