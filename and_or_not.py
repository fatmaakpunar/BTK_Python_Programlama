#girilen sayı 0 ile 100 arasında mı
# sayi = float(input('sayi: '))
# result = (sayi>0 and sayi<100)
# print(f'girilen sayının 0-100 arasında olma durumu {result}')

#girilen sayı pozitif çift sayı mı
# sayi = float(input('sayi: '))
# result = (sayi>0 and (sayi%2 == 0))
# print(f'girilen sayının pozitif çift sayı olma durumu: {result}')

#email ve parola kontrol
# email = 'fatmaakpunar42@gmail.com'
# parola = '123456'
# emailgirdi = str(input('email: '))
# parolagirdi = str(input('parola: '))
# result = (emailgirdi == email and parolagirdi == parola)
# print(f'email ve şifreniz: {result}')

#girilen 3 sayıyı büyüklük olarak karşılaştırınız
# sayi1 = int(input('sayi1: '))
# sayi2 = int(input('sayi2: '))
# sayi3 = int(input('sayi3: '))
# result = ((sayi1>sayi2) and (sayi1>sayi3))
# print(f'a en büyük sayı mı? => {result}')

#kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız eğer ortalama 50 ve üstüyse geçti değilse kaldı yazdırın
# vize_1 = float(input('1. vize: '))
# vize_2 = float(input('2. vize: '))
# final = float(input('final: '))
# ortalama = (((vize_1 + vize_2) / 2)*0.6) + (final*0.4)
# #ortalama 50 olsa bile final en az 50 olmalı
# # result = ((ortalama>=50) and (final>=50))
# # print(f'geçme durumu:{result}')
# #finalden 70 alırsa ortalama şartı kalksın
# result = ((ortalama>=50) or (final>=70))
# print(f'geçme durumu:{result}')

#kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız
#formül: (kilo/ boy)**2
#şartlar 
# 0-18.4 zayıf
# 48.5-24.9 normal
# 25-29.9 fazla kilolu
# 30-34.9 obez
name = input('name: ')
kilo = float(input('kilo '))
boy = float(input('boy: '))
index = (kilo) / (boy**2)
zayif = ((index>=0) and (index<=18.4))
normal = ((index>=18.5) and (index<=24.9))
fazla = ((index>=25.0) and (index<=29.9))
obez = ((index>=30.0) and (index<=34.9))
print(f'sayın {name} indexe göre durumuzuz zayıf: {zayif}  ')
print(f'sayın {name} indexe göre durumuzuz normal: {normal} ')
print(f'sayın {name} indexe göre durumuzuz fazla kilolu: {fazla}')
print(f'sayın {name} indexe göre durumuzuz obez: {obez}')