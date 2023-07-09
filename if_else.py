#1-kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet 
#alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#lise ya da üniversite olmalıdır.
# name = str(input("isminiz: "))
# age = int(input("yaşınız: "))
# education = str(input("eğitim durumunuz: "))
# if (age>=18) and (education == "lise" or education=="üniversite") :
#     print("TEBRİKLER EHLİYET ALABİLİRSİNİZ")
# else:
#         print("MALESEF EHLİYET ALAMAZSINIZ :(")

#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
# not aralığına karşılık gelen not bilgisini yazdırınız.
#0-24 => 0
#25-44 => 1
#45-54 => 2
#55-69 => 3
#70-84 => 4
#85-100 => 5
# sinav_1 = int(input("1. sınav notunuzu giriniz: "))
# sinav_2 = int(input("2. sınav notunuzu giriniz: "))
# sözlü = int(input("sözlü notunuzu giriniz: "))
# ortalama = (sinav_1+sinav_2+sözlü)/3
# if 0<=ortalama<=24:
#     print(f"ortalamanız {ortalama} notunuz 0")
# elif 25<=ortalama<=44:
#     print(f"ortalamanız {ortalama} notunuz 1")
# elif 45<=ortalama<=54:
#     print(f"ortalamanız {ortalama} notunuz 2")
# elif 55<=ortalama<=69:
#     print(f"ortalamanız {ortalama} notunuz 3")
# elif 70<=ortalama<=84:
#     print(f"ortalamanız {ortalama} notunuz 4")
# elif 85<=ortalama<=100:
#     print(f"ortalamanız {ortalama} notunuz 5")
# else:
#     print("geçersiz değer kontrol ediniz")

#3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#1. Bakım => 1. yıl
#2. Bakım => 2. yıl
#3. Bakım => 3. yıl
#**Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#*** datetime modülünü kullanmanız gerekiyor..
#(simdi) (2018/8/1) => gün
# import datetime
# tarih = input("aracınız hangi tarihte trafiğe çıktı (2019/8/9): ")
# tarih= tarih.split('/')
# trafigecikis = datetime.datetime(tarih[0], tarih[1], tarih[2])
# simdi = datetime.datetime.now()
# fark = simdi - trafigecikis
# days= fark.days

# if days <= 365:
#     print("1. servis aralığı")
# elif days>365 and days<=365*2:
#     print("2. servis aralığı")
# elif days>365*2 and days<=365*3:
#     print("3. servis aralığı")
# else:
#     print("hatalı değer")
