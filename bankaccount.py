class Account():

    def __init__(self):
        owner = input("Enter Your Name: ")
        self.__name = owner
        amt = input("Enter Your Amount: ")
        amount = int(amt)
        self.__amount = amount
        print("Account Created successfully")

    def __deposit(self,amt):
        self.__amount = self.__amount+amt
        print(f'money deposited successfully... {self.__amount}')
       

    def __withdraw(self,amt):
        if amt<self.__amount:
            self.__amount = self.__amount-amt
            print(f'Withdraw successfully...new balace is: {self.__amount}')
           
        else:
            temp = amt-self.__amount
            print(f'not enough money to withdraw ...please deposit first {temp}')
            


    def Accountintialise(self):
        while True:
            print("\n")
            print("2.Deposit Amount")
            print("3.Withdraw Amount")
            print("Enter any other key to exit: ")
            i = input("Enter Your Choice: ")
            x = 0
            if i.isdigit():
                x = int(i)

        

            if x==2:
                amt = input("Enter Amount to Deposit: ")
                amount = int(amt)
                a.__deposit(amount)

            elif x==3:
                amt = input("Enter Amount to Withdraw: ")
                amount = int(amt)
                a.__withdraw(amount)

            else:
                print("Thank You!")
                break
            
        
