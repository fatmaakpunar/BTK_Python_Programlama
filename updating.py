# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt", "r+", encoding="utf-8") as file:#r+ hem okuma hem yazmayı temsil eder
#     print(file.read()

#*********sayfa sonunda güncelleme***********

# with open("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nKadir Akpunar") 

#***********sayfa başında gğncelleme***********
# with open("newfile.txt", "r+", encoding="utf-8") as file:
#      content =file.read()
#      content = "Hi <3 \n" + content
#      file.seek(0)
#      file.write(content)

#***********sayfa ortasında gğncelleme***********
with open("newfile.txt", "r+", encoding="utf-8") as file:
    list= file.readlines()
    list.insert(1, "Yılmaz Aygün \n")
    file.seek(0)
    file.writelines(list)
    
    for i in list:
        file.write(i)
with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())