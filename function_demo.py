#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 
# def goster(kelime, adet):
#    print(kelime*adet)
# goster('Merhaba\n',10)

#2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın. 
# def cevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)
#     return liste
# result = cevir(10,20,30,'merhaba')  
# print(result)  

#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun. 
# def asalSayılariBul(sayil, sayi2):
#  for sayi in range(sayil, sayi2+1):
#   if sayi > 1:
#    for i in range(2, sayi):
#     if (sayi % i == 0): 
#       break
#    else:
#     print(sayi)
# sayil = int(input('sayı 1:'))
# sayi2= int(input('sayı 2:'))
# asalSayılariBul (sayil, sayi2)

#4-Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür
def tam(sayi1):
    liste =[]
    for i in range(2, sayi1):
        if sayi1%i==0:
            liste.append(i)
    print(liste)
sayi1=int(input("sayı1:"))
tam(sayi1)
    
