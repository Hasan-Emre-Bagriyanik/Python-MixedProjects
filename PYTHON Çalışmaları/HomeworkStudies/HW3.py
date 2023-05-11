

from gettext import dgettext
from this import d


def q1():
    #Kullanıcıdan bir sayının mükemmel olup numune yerleştirmek için.

    #Bir sayının kendi hariç bölenlerinin kendine göre sayılırse bu sayıya "mükemmel sayı" denir.
    #  Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

    number = int(input("Enter a number: "))

    i=1
    total = 0
    while i < number :
        if number % i == 0:
            total += i
        i +=1

    if total == number:
        print("Perfect number...")

    else:
        print("It is a not perfect number...")
 

#q1()     



def q2():


    """Kullanıcıdan bir sayı sayısı "Armstrong olacak şekilde belirlenecek.

    Örnek olarak, Bir sayı sayı 4 basamaklı ise ve çevresinden herbirinin 4.ninden( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

    Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
    """

    
    number = input ( "Enter a number: " )

    digit_Number = len(number)
    number = int(number)
    digit = 0
    total = 0

    temp_number = number 

    while temp_number > 0 :
        digit = temp_number % 10
        total += digit ** digit_Number

        temp_number //= 10

    if total == number:
        print(number , " is an armstrong number...")

    else:
        print(number , " is not an armstrong number...")

#q2()




def q3():


    #Onun bir iken satın alınabilirde bir numara alın ve satın almak için "toplam" isimli bir süslemeye ekleyin. Kullanıcı "q" bastığı zamanlamayı bitirin ve "toplamını" bastırın.

    #İpucu : iken kullanımq'ya başarsayü mola ile sonlandırın.

    print("Press 'q' to log out...")


    total = 0

    while True:
        number = input("Enter a number: ")
    
        if number == "q":
            print("log out...")
            break
        number = int(number)
        total += number
       

    print("Total: " , total)

#q3()


def q4():

    #1'den 100'e kadar olan sayılardan 3'e bölünenlerden bahsedin. Bu işlemi ile devam etmeye çalışın.

    for i in range(101):
        if i % 3 == 0 :
            print(i)

#q4()


def q5():

    #problemin çözümlerinden ürünlerimizde özellikle öğrenmedik. Burada mantık yürüterek ve 
    # liste anlama kullanarak 1'den 100 olan sayılardan sadece çifte bir listeye atmayı yapmayı deneyin.
    
    #list1 = [list(range(1,101))]


    
    list  =  [ x  for  x  in  range( 1 , 101 ) if x % 2 == 0 ]
    print ( list ) 
    




q5()
