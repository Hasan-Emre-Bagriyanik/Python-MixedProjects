

def q1():
    
    liste = [345,"sadas","324a",14,"kemal"]

    for s in liste:
        try:
            if(type(s) == int):
                print("Number: " , s)
        except:
            raise ValueError("Error...")

#q1()



def q2():

    def cift_mi(sayi):
    
        if (sayi % 2 == 0):
            return sayi
        else:
            raise ValueError
    liste = [34,2,1,3,33,100,61,1800]

    for i in liste:
        try:
            print(cift_mi(i))
        except ValueError:
            pass



#q2()
                
   

def q3():

   q = 1
   p = 0
   r = 0

   print((p and q) or (r and p))
   



q3()
