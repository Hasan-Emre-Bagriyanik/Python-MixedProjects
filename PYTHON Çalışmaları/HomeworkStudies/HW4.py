

def q1():
#'den 1000'e kadar olan sayılardan mükemmel değer okuma kaydının. Bunun için bir sayının mükemmel olup dönüşen bir tane fonksiyonunda.

#Bir sayının bölenlerinin kendi kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1+2+3=6).


    def perfect(number):

        total = 0

        for i in range(1,number):
            if number % i == 0 and number != i:
                total += i
            
        return  total == number
            
    number = input("Enter a number: ")

    while True:  
    
        if number == "q":
            print("log out...")
            break

        else:
            number = int(number)
            for i in range(1,number+1):
                if perfect(i):
                    print("Perfect number: ",i)
        break


#q1()



def q2():

    #Kullanıcıdan 2 tane sayı bu kişinin en büyük bölenini (EBOB) dönen bir tane işlevi yazın.


    def find_ebob(number1,number2):

        i = 1
        ebob = 1

        while ((1 <= number1))  and  (1 <= number2):

            if (not (number1 % i)  and  not (number2 % i)):

                ebob = i

            i += 1
        return ebob

    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))

    print("EBOB: ",find_ebob(number1,number2))


#q2()


def q3():

    def find_ekok(num1,num2):
        i = 2
        ekok = 1
        while True:
            if(num1 % i == 0)  and (num2 % i== 0):
                ekok *= i

                num1 //= i
                num2 //= i
            
            elif (num1 % i == 0)  and (num2 % i != 0):
                ekok *= i

                num1 //= i

            elif (num1 % i != 0)  and (num2 % i == 0):

                ekok *= i

                num2 //= i

            else:
                i += 1

            if(num1 == 1 )  and  ( num2 == 1):
                break

        return ekok

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))


    print("EKOK: ",find_ekok(num1,num2))


#q3()


def q4():

    #Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

    birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

    def read(num):

        first = num % 10 
        second = num // 10

        return onlar[second] + " " + birler[first]

    num = int(input("Enter a number: "))

    print("Read a number: " ,read(num))

        
q4()







