
def q1() :

    #Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    product = a*b*c
    print("Products of number: {} x {} x {} = {}".format(a,b,c,product))    

q1()


def q2() :
    #Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
    #Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

    height = float(input("Enter your height(m): "))
    weight = int(input("Enter yout weight(kg): "))

    BKİ = weight/ height**2

    print("Body mass index: " ,BKİ)

#q2()


def q3() :
    # Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini
    #  alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.


    fuel = float(input("How many kilometer does it burn: "))
    km = int(input("How many kilometers did you go(km): "))

    total = fuel * km 
    print("Fee due : " ,total, "TL")
#q3()


def q4() : 
   #Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

    name = input("your name: ")
    surname = input("your surname: ")
    number = input("your number: ")

    print("Name: {}\nSurname: {}\nNumber: {}".format(name,surname,number))


#q4()


def q5() :
     #Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    print(a,b)

    a , b = b, a

    print(a,b)

#q5()


def q6() :
    #Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
    #Hipotenüs Formülü: a^2 + b^2 = c^2

    firstEdge = int(input("Enter the first edge: "))
    secondEdge = int(input("Enter the second edge: "))

    hypotenuse = (firstEdge ** 2 +secondEdge**2 ) **0.5
    print("Hypotenuse: ",hypotenuse)

#q6()