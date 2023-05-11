print("""

USER LOGIN

""")

sys_userName = "Hasan Emre"
sys_password = "12345"
right_of_entry = 3

while True:
    UserName = input("Enter user name:")
    password = input("Enter password:")

    if(UserName == sys_userName  and  password != sys_password) :
        print("Password wrong...")
        right_of_entry -= 1

    elif(UserName != sys_userName  and  password == sys_password) :
        print("User name wrong...")
        right_of_entry -= 1

    elif(UserName != sys_userName  and  password != sys_password) :
        print("User name wrong and password wrong...")
        right_of_entry -= 1

    else: 
        print("Welcome...") 
        break

    if right_of_entry == 0 :
        print("your login has expired...")
        break