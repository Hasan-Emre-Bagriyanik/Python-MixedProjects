

def q1() :

    """
Kullanıcılardan alınan boy ve kilo değerlerine göre kitle indeksini hesaplayın ve şu şekildeki şu yazıları tarihin izini sürüyor.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez   """



    height = float(input("Enter your height(m): "))
    weight = int(input("Enter yout weight(kg): "))

    BKİ = weight/ height**2

    print("Body mass index: " ,BKİ)

    if BKİ <= 18.5 :
        print("Weak...")

    elif 18.5 <= BKİ and BKİ <= 25 :
        print("Normal...")

    elif 25 <= BKİ and BKİ <= 30:
        print("Overweight...")
    
    elif  BKİ >= 30 :
        print("Fat...")

    else: 
        print("You have done wrong...")

#q1()
    


def q2():
    #Kullanıcıdan 3 tane sayı ve en büyük sayıyı yazdırın.

    a = int(input("Frist number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))

    if a >= b  and  a >= c :
        print("Largest number: ", a )

    elif b >= a and  b >= c :
        print("Largest number: ", b )

    else:
        print("Largest number: ", c )

#q2()



def q3(): 
    """
    Kullanıcının vize1,vize2, hesaplarına göre harf notlarını hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
    """


    exam1 = int(input("First exam: "))
    exam2 = int(input("Second exam: "))
    final = int(input("Final exam: "))

    average = ((exam1*0.3) + (exam2*0.3) + (final*0.4))

    print("average: ", average)

    if average >= 90 :
        print("AA")

    elif 90 >= average and average >= 85 :
        print("BA")

    elif 85 >= average and average >= 80 :
        print("BB")

    elif 80>= average and average >= 75 :
        print("CB")

    elif 75 >= average and average >= 70 :
        print("CC")

    elif 70 >= average and average >= 65 :
        print("DC")

    elif 65 >= average and average >= 60 :
        print("DD")

    elif 60 >= average and average >= 55 :
        print("FD")
    
    else:
        print("FF")
    
#q3()


