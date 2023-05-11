
import math


def q1():
    #Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.


    print("""
    

        GELİŞMİŞ HESAP MAKİNASI

        ADVENCED CALCULATOR
    
    
    Press 'q' to log out...

    Process;

    1.Summation process (Toplama işlemi)

    2.extraction process (Çıkarma işlemi)

    3.Divide process (Bölme işlemi)

    4.multiplication (Çarpma işlemi)

    5.exponentiation (üs alma)

    6.take a square root (Karekök alma)
    
    
    """)


    process = input("Enter a process: ")


    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))



    if(process =="q"):
        print("Exiting program...")
        return

    elif process == "1":
        print("collections: {} + {} = {}".format(a,b,a+b))

    elif process == "2" : 
        print("extraction: {} - {} = {}".format(a,b,a-b))

    elif process == "3" : 
        print("Episode: {} / {} = {}".format(a,b,a/b))

    elif process == "4" : 
        print("Product: {} * {} = {}".format(a,b,a*b))

    elif process == "5":
        print("Exponentiation:: " ,math.pow(a,b))

    elif process == "6":
        print("Spuare root: ",math.sqrt(a))

    else:
        print("You made the wrong choice...")
            
q1()



