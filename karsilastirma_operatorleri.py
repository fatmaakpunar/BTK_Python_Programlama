#girilen 2 sayıdan hangisi büyüktür?
# a = int(input('a: '))
# b = int(input('b: '))
# result = (a>b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

#kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız eğer ortalama 50 ve üstüyse geçti değilse kaldı yazdırın
# vize_1 = float(input('1. vize: '))
# vize_2 = float(input('2. vize: '))
# final = float(input('final: '))
# ortalama = (((vize_1 + vize_2) / 2)*0.6) + (final*0.4)
# print(f'not ortalamanz {ortalama} ve dersten geçme durumunuz {ortalama>50}')

#girilen bir sayının tek mi çift mi olduğunu yazdırın.
# sayi = int(input('sayi: '))
# tekcift = (sayi % 2 == 0)
# print(f'girilen sayının çift olma durumu: {tekcift}')

#girilen bir sayının negatif pozitif olma durumu
# sayi = int(input('sayi: '))
# isaret = (sayi<0)
# print(f'girilen sayının negarif olma durumu: {isaret}')

#parola ve email bilgisini isteyip doğruluğunu kontrol ediniz
email = str(input('email: '))
sifre = str(input('sifre: '))
email_kontrol = (email == 'fatmaakpunar42@gmail.com')
sifre_kontrol = (sifre == '123456')
print(f'girdiğiniz email: {email_kontrol} ve şifre: {sifre_kontrol}')