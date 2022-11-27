class SbiAtmClass:
    acBal = 0
    exit = "N"

    def __init__(self, name):
        self.name = name

    def greet_user(self):
        print(f'''
*********************************
Welcome to SBI {self.name.upper()}
*********************************
Your Account bal is :Rs.{self.acBal}
You Can Use Following Actions :''')

    def update(self, transaction_amount, action):
        if action == 1:
            print(f'''
-----------------------------------
Account Credit with Rs.{transaction_amount}''')
            print(f'''
Updated Bal:Rs.{self.acBal}
-----------------------------------''')
        elif action == 2 or action == 3:
            print(f'''
-----------------------------------
Account debited with Rs.{transaction_amount}''')
            print(f'''
Updated Bal:Rs.{self.acBal}
------------------------------------''')

    def transaction(self):

        while self.exit.upper() == "N":
            print(f'''
1) Deposit Cash 
2) Withdraw Cash
3) Transfer Cash ''')
            action = int(input("Please choose one to proceed further : "))

            if action == 1:
                transaction_amount = int(input('How much do you want to deposit ? : '))
                self.acBal += int(transaction_amount)
                self.update(transaction_amount, action)
                self.exit = input('Do you want to exit ? : (Y/N) ')

            elif action == 2:
                transaction_amount = int(input('How much do you want to withdraw ? : '))
                if self.acBal != 0:
                    self.acBal -= int(transaction_amount)
                    self.update(transaction_amount, action)
                    self.exit = input('Do you want to exit ? : (Y/N) ')

            elif action == 3:
                transaction_amount = input('How much do you want to Transfer ? : ')
                if self.acBal != 0:
                    self.acBal -= int(transaction_amount)
                    self.update(transaction_amount, action)
                    self.exit = input('Do you want to exit ? : (Y/N) ')

    def exitGreet(self):
        print(f'''
        ***  Thank You for Banking with us Mr.{self.name} visit again  ***''')
