



class Developer():

    def __init__(self,name,surname,number,wage,languages) :
        self.name = name
        self.surname = surname
        self.number = number
        self.wage = wage
        self.languages = languages


    def showInformation(self):
        print("""
        Properties of the developer object

        Name = {}

        Surname = {}

        Number = {}

        Wage = {}

        Languages = {}
        
        """.format(self.name,self.surname,self.number,self.wage,self.languages))

    def make_raise(self,raise_amount):
        print("Make a raise...")

        self.wage += raise_amount

    def add_language(self,new_language):
        print("Adding a new languages...")

        self.languages.append(new_language)




developer = Developer("Hasan Emre","Bağrıyanık",1210505023,25000,["C , C++ , C# , Java , Python , html ,CSS"])

developer.showInformation()

developer.add_language("PHP")
developer.make_raise(5000)

developer.showInformation()

