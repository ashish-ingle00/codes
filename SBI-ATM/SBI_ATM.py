name = input("Enter Your Name : ")
ac_bal = 0

print(f''' 
*********************************
   Welcome to SBI {name.upper()}
*********************************
Your Account bal is :Rs.{ac_bal}
You Can Use Following Actions :''')
exit = 'N'

while exit.upper()=='N':
    print(f'''
1) Deposit Cash 
2) Withdraw Cash
3) Transfer Cash 
''')
    action = input("Please choose one to proceed further :(Choose Number) ")
    if action == "1":
        add = int(input('How much do you want to deposit ? : '))
        ac_bal += add
        print(f'''
-----------------------------------      
Account Credited with Rs.{add}''')
        print(f'''Updated Bal :Rs.{ac_bal}
------------------------------------''')

    elif action == "2":
        withdraw = int(input('How much do you want to withdraw ? : '))
        if ac_bal != 0:
            ac_bal -= withdraw
        print(f'''
-----------------------------------      
Account debited with Rs.{withdraw}''')
        print(f'''Updated Bal :Rs.{ac_bal}
------------------------------------''')

    elif action == "3":
        minus = input('How much do you want to Transfer ? : ')
        if ac_bal != 0:
            ac_bal -= int(minus)
        print(f'''
-----------------------------------      
Account debited with Rs.{minus}''')
        print(f'''Updated Bal :Rs.{ac_bal}
------------------------------------''')

    exit=input('Do you want to exit ? : (Y/N) ')
print(f'''

***  Thank You for Banking with us Mr.{name.upper()} visit again  ***
''')


