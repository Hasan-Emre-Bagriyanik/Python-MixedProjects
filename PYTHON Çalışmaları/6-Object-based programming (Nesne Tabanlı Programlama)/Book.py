



class Book():
    def __init__(self,name,author,num_page,type) :
        print("The book class running")
        self.name = name
        self.author = author
        self.num_page = num_page
        self.type = type

    def __str__(self) :
        return ("name: {}\nAuthor: {}\nNumber of pages: {}\nType: {}\n".format(self.name,self.author,self.num_page,self.type))


    def __len__(self):
        return self.num_page


    def __del__(self):
        print("book object is deleted...")



book = Book("İstanbul Hatırası" ,"Ahmet Ümit", 561,"Polisiye" )

print(book)

len(book)

del book