bankdb={1000:{"accno":1000,"name":"Ramesh","balance":20000}}

class Bank:
    def create_account(self,accno,name,minbalance):
        self.accno=accno
        self.name=name
        self.minbalance=minbalance

    def deposit(self,amt,accno):
        self.minbalance+=amt
        print(amt," CREDITED TO ACCOUNTNO ",self.accno,".AVAILABLE BALANCE - ",self.minbalance)
    def withdrawal(self,amt,accno):
        if amt>self.minbalance:
            print("INSUFFICIENT FUNDS!")
        else:

            self.minbalance-=amt
            print(amt," DEBITED FROM ACCOUNTNO ",self.accno,".AVAILABLE BALANCE - ",self.minbalance)
    def accdetails(self):
        print("Account number -",self.accno)
        print("Name - ",self.name)
        print("Available balance - Rs.",self.minbalance)
obj = Bank()
c="y"
acc=1000
while(c == "y"):

    print("MY BANK")
    print("press 1 for Account creation")
    print("press 2 for Deposit")
    print("press 3 for Withdrawal")
    print("press 4 for Account Details")
    a=int(input())
    if a==1:
        name=input("enter name:")
        minbalance=int(input("enter minimum balace:"))
        obj.create_account(accno=acc,name=name,minbalance=minbalance)
        acc+=1
    elif a==2:
        accnum=(int(input("Enter Account Number")))
        if accnum in dict:
            camount=int(input("enter amount to be deposited:"))
            obj.deposit(amt=camount,accno=accnum)
    elif a==3:
        accnum = (int(input("Enter Account Number")))
        if acc in dict:
            damount = int(input("enter amount to be Withdrawn:"))
            obj.withdrawal(amt=damount)
    elif a==4:

        obj.accdetails()
    c=input("Do you wish to continue?[y/n]")