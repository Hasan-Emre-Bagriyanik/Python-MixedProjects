print("""

USER LOGIN

""")

sys_userName = "Hasan Emre"
sys_password = "12345"
UserName = input("Enter user name:")
password = input("Enter password:")

if(UserName == sys_userName  and  password != sys_password) :
    print("Password wrong...")

elif(UserName != sys_userName  and  password == sys_password) :
    print("User name wrong...")

elif(UserName != sys_userName  and  password != sys_password) :
    print("User name wrong and password wrong...")

else: 
    print("Welcome...") 