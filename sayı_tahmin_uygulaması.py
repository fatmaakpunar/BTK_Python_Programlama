# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
# **"random modülü" için "python random" şeklinde arama yapın.
# **100 üzerinden puanlama yapın. Her soru 20 puan.
# **Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
import random
sayi = random.randint(1,100)
can = int(input('kaç hakkınız olsun: '))
hak = can
sayac=0
while hak>0:
    hak -= 1
    sayac +=1
    tahmin_sayi = int(input('Bir sayı tahmin edin:'))
    if sayi>tahmin_sayi:
      print('YUKARI')
    elif sayi==tahmin_sayi:
     print(f'TEBRİKLER {sayac}. DEFADA BİLDİNİZ. TOPLAM PUANINIZ: {100-(100/can)*(sayac-1)}')
     break
    elif sayi<tahmin_sayi:
     print('AŞAĞI')
    
     if hak == 0:
       print(f"hakkınız bitti tutulan sayı: {sayi}")