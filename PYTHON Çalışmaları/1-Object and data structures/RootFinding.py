

print("SECOND DEGREE ROOT FINDING (İKİNCİ DERECEDEN KÖK BULMA)")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b**2 -4*a*c

if(delta >= 0) :

    X1 = -b - delta **0.5
    X2 = -b + delta **0.5
    print("First root: {}\nSecond root: {}".format(X1,X2))

else :
    print("no root(kök bulunmamaktadır)")






