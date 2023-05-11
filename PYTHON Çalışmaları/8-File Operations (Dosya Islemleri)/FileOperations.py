
"""file  = open("C:/Users/Hasan Emre/Desktop/Informations.txt","w", encoding="utf-8")

file.write("Hasan Emre Bağrıyanık")
file.close()

file  = open("C:/Users/Hasan Emre/Desktop/Informations.txt","w", encoding="utf-8")#'w' parametresini kullandığımız için dosya her defasında silinip tekradan yazılır

file.write("Hasan Emre Bağrıyanık\n")#Dosyaya bir şeyler yazıyoruz
file.write("Mehmet Ali Sivri\n")
file.write("Hasan Emre Bağrıyanık\n")
file.write("Mehmet Ali Sivri\n")
file.write("Hasan Emre Bağrıyanık\n")
file.write("Mehmet Ali Sivri\n")
file.close()

file = open("C:/Users/Hasan Emre/Desktop/Informations.txt","r",encoding="utf-8")
for i in file:#For döngüsü ile dosyayı baştan sona kadar okur
    print(i,end="")
file.close()

file = open("C:/Users/Hasan Emre/Desktop/Informations.txt","r",encoding="utf-8")
contents = file.read()#Dosyayı baştan sona okur
print("The file contents(Dosya içeriği): ")
print(contents)
contents2 = file.read()#Dosya bir kere okundu ve imleç en alta geldiği için ikinci kez okuma yapmaz
print("The file contents: ")
print(contents2)

file = open("C:/Users/Hasan Emre/Desktop/Informations.txt","r",encoding="utf-8")
print(file.readline())#Dosyadan tek tek satırları okur
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


file = open("C:/Users/Hasan Emre/Desktop/Informations.txt","r",encoding="utf-8")

list = file.readlines()#Burada dosya liste şeklinde okunuyor 
print(list)
file.close()"""


with open("C:/Users/Hasan Emre/Desktop/Informations.txt","r",encoding="utf-8") as file:#dosyayı otomatik olarak kapatıyor
    file.seek(5)#İmlecin nereye gideceğini söylüyor
    contents = file.read(10)
    print(contents)
    print(file.tell())#İmlecin nerde olduğunu söylüyor



