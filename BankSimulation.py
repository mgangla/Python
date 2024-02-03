##defn class Bank account with private attributes

 
class BankAccount :
    def _init_(self,name,balance):
        self.__name = name
        self.__balance= balance 
        balance =50000
        self.bank =[]

    
        def get_balance (self):
        #retrieve the current balance
                print("\n Current Balance =",{self.__balance}) #



        def check_balance (self):
                print("\n Account Name :{self.__name} ,balance {self.__balance}")
        

        def deposit (self,amount) :
                amount = float(input("Enter amount to be deposited: "))
                self.__balance += amount
                print("\n Amount Deposited:", amount)

        def withdraw (self,amount) :
                amount = float(input("Enter amount to be withdrawn: "))
                if self.__balance >= amount:
                        self.__balance -= amount
                        print("\n You Withdrew:", amount)
                else:
                        print("\n Insufficient balance  ")

        #Function for appreciation
        def thanks(self):
                print("Thank you for being a member =")
                print("Goodbye")

#execute the code
#instance of the bank account object
        
        myBankAccount = BankAccount()


  
# Calling functions with that class object
        print(myBankAccount.get_balance())
        myBankAccount.check_balance()
        myBankAccount.deposit()
        myBankAccount.withdraw()
        myBankAccount.thanks()

