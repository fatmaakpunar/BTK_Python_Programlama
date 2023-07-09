#1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# sayi = int(input("bir sayı giriniz: "))
# if sayi>=0 and sayi<=100:
#     print("sayı 0-100 aralığındadır")
# else:
#     print("sayi 0-100 aralığında değildir")

#2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# sayi = int(input("bir sayı giriniz: "))
# if sayi>0:
#     if sayi%2==0:
#       print("sayı pozitif çift sayıdır")
#     else:
#        print("sayı pozitif ancak çift değildir")
# else:
#    print("sayı pozitif değildir")


#3-e-mail ve parola bilgileri ile giriş kontrolü yapınız.
# email = "fatmaakpunar42@gmail.com"
# sifre = "123456"
# emailgirdi = input("e-mail: ")
# sifregirdi = input("sifre: ")
# if email == emailgirdi:
#     if sifre == sifregirdi:
#         print("e-mail ve şifre bilgileri doğru")
#     else:
#         print("şifre bilgisi yanlış")
# else:
#     print("e-mail bilgisi yanlış")

#4-girilen 3 sayıyı büyüklük olaraka karşılaştırınız
# a = int(input("1. sayıyı giriniz: "))
# b = int(input("2. sayıyı giriniz: "))
# c = int(input("3. sayıyı giriniz: "))
# if a>b and a>c:
#     print("1. sayı büyüktür")
# elif b>a and b>c:
#     print("2. sayı büyüktür")
# elif c>a and c>b:
#     print("3. sayı büyüktür")
# else:
#     print("sayılar eşit veya hata")

#5-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. 
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın. 
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#  b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# vize1 = int(input("1. vize notu: "))
# vize2 = int(input("2. vize notu: "))
# final = int(input("final notu: "))
# ortalama = (((vize1+vize2)/2)*0.6) + (final*0.4)
# if ortalama>=50 and final>=50:
#     print(f"Öğrencinin ortalaması {ortalama} => GEÇTİ")
# elif final>=70:
#     print(f"Öğrencinin ortalaması {ortalama} => GEÇTİ")
# else:
#     print(f"Öğrencinin ortalaması {ortalama} => KALDI")

#6-Kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız
#formül: (kilo/ boy)**2
#şartlar 
# 0-18.4 zayıf
# 48.5-24.9 normal
# 25-29.9 fazla kilolu
# 30-34.9 obez
name = input('name: ')
kilo = float(input('kilo: '))
boy = float(input('boy: '))
index = (kilo) / (boy**2)
if 0<index<18.4:
    print(f"Sayın {name} İndex değeriniz {index} ve durumunuz => ZAYIF")
elif 18.5<index<24.9:
    print(f"Sayın {name} İndex değeriniz {index} ve durumunuz => NORMAL")
elif 25.0<index<29.9:
    print(f"Sayın {name} İndex değeriniz {index} ve durumunuz => FAZLA KİLOLU")
elif 30.0<index<34.9:
    print(f"Sayın {name} İndex değeriniz {index} ve durumunuz => OBEZ")
else:
    print("HATA")