##defn class Bank account with private attributes

 
class BankAccount:
        def __init__(self,name,balance):
                self.__name = name
                self.__balance= balance 
                
    
        def get_balance (self):
        #retrieve the current balance
                return(f" Current Balance = {self.__balance}") 



        def check_balance (self):
                return(f" Account Name :{self.__name} ,balance {self.__balance}")
        

        def deposit (self) :
                amount = float(input("Enter amount to be deposited: "))
                self.__balance += amount
                return(" Amount Deposited:", amount)

        def withdraw (self) :
                amount = float(input("Enter amount to be withdrawn: "))
                if self.__balance >= amount:
                        self.__balance -= amount
                        return("\n  You Withdrew:", amount)
                else:
                        return("\n Insufficient balance  ")

        #Function for appreciation
        def thanks(self):
                return("Thank you for being a member")

#execute the code
#instance of the bank account object

myBankAccount = BankAccount("John", 2000)


  
# Calling functions with that class object
print(myBankAccount.get_balance())
print(myBankAccount.deposit())
print(myBankAccount.withdraw())
print(myBankAccount.check_balance())
print(myBankAccount.thanks())

