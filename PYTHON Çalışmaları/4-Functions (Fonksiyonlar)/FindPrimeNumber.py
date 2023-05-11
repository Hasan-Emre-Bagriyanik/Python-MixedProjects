
print("""

ASAL SAYI BULMA

FIND PRIME NUMBER

Press 'q' to log out...


""")


def primeNumber(number):

    if number == 0:
        return False

    elif number == 1:
        return False

    else:
        for i in range(2,number):
            if number %i == 0:
                return False
            
        return True



while True:
    number = input("Enter a number: ")

    if number == "q":
        print("Log out...")
        break

    else:
        number = int(number)
        if primeNumber(number):
            print("Prime number...")
            
        else:
            print("Not prime number...")