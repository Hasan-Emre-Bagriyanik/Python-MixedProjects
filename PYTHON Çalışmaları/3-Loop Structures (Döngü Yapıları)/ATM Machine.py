
print("""

WELCOME TO ATM MACHİNE

Process;

1-Balance learning

2-Whitdraw Money

3-Deposit money

Press 'q' to log out...

""")

balance = 1000

while True:

    process = input("Select a process: ")

    if process == "q":
        print("log out")
        break


    elif process == "1":
        print("Your balance: {} ".format(balance))


    elif process == "2":
        total = int(input("Enter a total: "))

        if balance <= total:
            print("you have insuficient balance...")
            continue    
        
        balance -= total
        print("Your balance: {}".format(balance))

    elif process == "3":
        total = int(input("Enter a total: "))

        balance += total 
        print("Your balance: {}".format(balance))

    else:
        print("You made the wrong selected...")
