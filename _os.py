import os
import datetime
# result = dir(os)
# result = os.name #kullandığımız işletim sistemini söyler nt=windows
# result =os.getcwd() #dosyanın hangi klasör içinde bulunduğunu söyler
# os.mkdir("newdirectory") #aynı klasör içinde "newdirectory" adında klasör oluşur 
# os.rename("newdirectory", "yeniklasör") #newdirectory dosyasının adını yeniklasör olarak değiştirir
# os.rmdir("yeniklasör")#yeni klasör dosyasını siler, alt klasörü olmaması lazım
# os.removedirs("newdirector/yeniklasör") #newdirector altındaki yeniklasör ü siler

#dizin değiştirme
# os.chdir('C:\\')
# os.chdir('..\..')
# os.mkdir("newdirectory")

# os.makedirs("newdirector/yeniklasör") #iç içe klasör oluşturur

#listeleme
# result = os.listdir() #klasördeki etkin dosyaları listeler 

#sadece py uzantılı dosyaları listelemek için
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# result = os.stat("date.py") #dosya hakkında bilgi verir
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) #oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) #son erişme tarihi

# os.system("notepad.exe") #istediğimiz dosyayı çalıştırır

#path
# result = os.path.abspath("_os.py") #dosyanın konumunu verir
# result = os.path.dirname("C:/Users/mervefatma/Desktop/python_temelleri") #dosyanın tam yolunu verir
# result = os.path.dirname(os.path.abspath("_os.py")) #dizin öğrenmek istiyorsunuz ama yolunu bilmiyorsunuz dosya adını biliyorsunuz o zaman dosyanın tam yolunu bulur dizin ismini alır
result = os.path.exists("C:/python/advanced-modules/_os1.py")
result = os.path.exists("C:/python/advanced-modules") 
result = os.path.isdir("C:/python/advanced-modules")
result = os.path.isfile("C:/python/advanced-modules/_os.py")
result = os.path.join("C:\\", "deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
#result = result[0]
result = result[1]

print(result)