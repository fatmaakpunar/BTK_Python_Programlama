#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#Kullanımı: open (dosya_adi, dosya_erisme_modu)
#dosya_erisme_modu=> dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu. 
#  **Dosyayı konumda oluşturur.
#  **dosya içeriğini siler ve yeniden ekleme yapr

# file = open("newfile.txt","w") #dosya otomatik oluşturulur
# file.close()

# file = open(" C:/Users/mervefatma/Desktop/newfile.txt","w")
# print(file)

#encoding = 'utf-8' => türkçe karakterler tanınsın diye
# file = open("newfile.txt", "w", encoding = 'utf-8')
# file.write("Fatma Akpunar")
# file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# 
# file.write("merve akpunar\n")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
file = open("newfile2.txt", "x",encoding='utf-8')

# "n": (Read) okuma. varsayılan, dosya konumda yoksa hata verir.