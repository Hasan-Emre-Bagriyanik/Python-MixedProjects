


liste = [345,"sadas","324a",14,"kemal"]

for s in liste:
    try:
        if(type(s) == int):
            print("Number: " , s)
    except:
        raise ValueError("Error...")


     


