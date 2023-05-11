print("""


FINDING FACTORIAL

press 'q' to log out...

""")


while True:
      number = input("Enter the number to get the factorial: ")

      if number == "q":
            print("Log out...")
            break

      else:
            number = int(number)
            factor = 1

            for i in range(2,number+1):
                  factor *= i
            print("Factorial: " , factor)