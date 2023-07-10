# sayilar = [1,3,5,7,9,12,19,21]

#1: sayilar listesini while ile ekrana yazdırın.
# i = 0
# while (i < len(sayilar)): #i değişkeni sayilar'ın eleman sayısından küçük olduğu sürece dönsün
#     print(sayilar[i])
#     i += 1

#2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
# bas = int(input("başlangıç sayısını giriniz: "))
# bit = int(input("bitiş sayısını giriniz: "))
# while bas < bit:
#     bas += 1
#     if(bas%2!=0):
#         print(bas)
    
#3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
# i = 100
# while i>0:
#     print(i)
#     i-= 1

#4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
# numbers = []
# i = 0
# while i<5:
#  sayi= int(input('sayı: '))
#  numbers.append(sayi)#yazılan sayıları numbers listesine ekler
#  i += 1
# numbers.sort()
# print(numbers)

#5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi icinde saklayınız
#   **ürün sayısını kullanıcıya sorun.
#   ** dictionary listesi yapısı (name, price) şeklinde olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler=[]
urun_sayi = int(input("listede kaç adet ürün bulunsun: "))
i=0
while i<urun_sayi:
    name =input("ürün ismi: ")
    price =input("ürün fiyatı: ")
    urunler.append({
        'name':name,
        'price':price
    })
    i += 1 #adet kadar ürün ekleyeceğimiz için
for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')