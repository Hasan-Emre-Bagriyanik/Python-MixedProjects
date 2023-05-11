

print("""*************************************

CALCULATOR PROGRAM

process;

1.Collection process

2.extraction process

3.Divide process

4.multiplication

""")

process = input("Enter process: ")
a = int(input("First number: "))
b = int(input("second number: "))



if process == "1":
    print("collections: {} + {} = {}".format(a,b,a+b))

elif process == "2" : 
    print("extraction: {} - {} = {}".format(a,b,a-b))

elif process == "3" : 
    print("Episode: {} / {} = {}".format(a,b,a/b))

elif process == "4" : 
    print("Product: {} * {} = {}".format(a,b,a*b))

else:
    print("Yanlış işlem yuaptınız...")




