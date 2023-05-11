

print("""

TAM BÖLEN BULMA

FİND DIVISOR

Press 'q' to log out...


""")



def findDivisor(number):

    exactFD = []

    for i in range(2,number):
        if number % i ==0:
            exactFD.append(i)

    return exactFD


while True:


    number = input("Enter a number: ")

    if number == "q":
        print("Log out...")
        break

    else:
        number = int(number)

        print("Find exact divisor: ", findDivisor(number))
        
