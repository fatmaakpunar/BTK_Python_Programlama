with open("newfile.txt", "r", encoding="utf-8") as file :#with kullanırken close fonksiyonuna ihtiyacımız yok otomatik kapanır
   content = file.read(10)
   print(content)
   file.seek(0) #cursor nereye gitsin, okumaya nereden başlasın
   print(file.tell()) #cursor(imleç) ün konumunu verir
   content2 =file.read()
   print(content2)#içerik gelmez çünkü imleç en sondaydı
