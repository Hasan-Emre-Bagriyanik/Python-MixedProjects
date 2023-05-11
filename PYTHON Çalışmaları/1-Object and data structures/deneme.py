from os import umask


print("Hello World")

a = ((10**2)//3)/3
print(a)


print(18//5)

print(15**2)
print(79**2)

a = "Emrenin bugün dersi var "

print(a[4:15])
print(len(a))

liste = ["merhaba",45,8,987]
print(liste)
print(len(liste))
print(liste[::-1])
print(liste[1::])


listeler = [45,87,84,96,48,21,35,57]
listeler.append(100)
print(listeler)
print(listeler.pop())
print(listeler)

print(listeler.pop(1))
print(listeler)

listeler.sort()
print(listeler)


demet = (1,2,3,3,4,5,6,7,8,9)
print(demet)
print(demet.count(3))
print("\n\n")

sozluk1 = {"bir":1,"iki":2,"üç":3,"dört":4}

print(sozluk1)
sozluk1["beş"]=5
print(sozluk1)
print(sozluk1["bir"])

sozluk1["beş"] += 10
print(sozluk1)

print(sozluk1.keys(),"\n")
print(sozluk1.values(), "\n")
print(sozluk1.items())

print("\n\n")

a = int(input("Birinci sayı:" ))
b = int(input("İkinci sayı:"))
c = int(input("Üçüncğ sayı:"))
print("Toplamları: ", a+b+c)

