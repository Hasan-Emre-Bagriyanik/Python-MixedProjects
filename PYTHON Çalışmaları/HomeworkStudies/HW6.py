


class Animal():

    def __init__(self,num_feet,color) :

        self.num_feet = num_feet
        self.color = color

    

    def number_feet(self):

        self.num_feet = input("Enter the number of feet: ")
        
        print("Number of feet: ",self.num_feet)
        

    def Color(self):

        self.color = input("Enter of color: ")
        
        print("Color: ",self.color)




class Dog(Animal):

    def __init__(self, num_feet, color,genus):

        super().__init__(num_feet, color)
        self.genus = genus


    def Genus(self,gen):

        gen = input("Enter a genus: ")
        self.genus = gen
        print("Genus: " , self.genus)


class bird(Animal):

    def __init__(self, num_feet, color, flying):

        super().__init__(num_feet, color)
        self.flying = flying


    def Flying(self):
        self.flying = input("Is the bird flying or not?(fly/not fly")
         
        if(self.flying == "fly"):
            print("Bird is flying...")
        else:
            print("Bird isn't flying...")
        

animal = Animal(4,"blue")
#animal.Color()
#animal.number_feet()
bird.Flying


        

        