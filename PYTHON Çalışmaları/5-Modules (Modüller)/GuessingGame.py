
# 1 ilke 40 arasında sayı tahmin oyunu
import random
import time


print("""

TAHMİN OYUNU

GUESSING GAME



""")

random_num = random.randint(1,40)
guess_right = 7

while True:

    guess = int(input("Enter a number: "))

  
    if(guess < random_num):
        print("your information is being queried...")
        time.sleep(1)

        print("Say higher number...")

        guess_right -= 1

    elif(guess > random_num):
        print("Your information is beign queried...")
        time.sleep(1)

        print("Say lower number...")
        guess_right -= 1

    else:
        print("your information is being queried...")
        time.sleep(1)

        print("congratulatory... Our number: " , random_num)
        break
    

    if(guess_right == 0):
        print("Your guess is over")
        print("Our number: ", random_num)
        break




        






