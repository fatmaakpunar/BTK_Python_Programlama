
# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()

file = open("newfile.txt", "r", encoding = "utf-8")

#for döngüsü

# for i in file:
#     print(i, end="")

#read() fonksiyonu
# content = file.read()
# print("içerik 1")
# print(content)

# file = open("newfile.txt", "r", encoding = "utf-8") #bunu yazmassak içerik2 nin içi boş olur imleç
# content2= file.read()
# print("içerik 2")
# print(content2)

# content =file.read(5) #ilk 5 karakter
# content =file.read(3)#ilk 5 karakterden sonraki 3 karakter
# print(content)

#************ readline() fonksiyonu

# print(file.readline(), end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

#************ readlines() fonksiyonu
# liste = file.readlines()
# print(liste)


file.close()