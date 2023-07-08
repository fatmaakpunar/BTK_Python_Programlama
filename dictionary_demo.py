# ogrenciler = {
# '120':{
#     'ad':'Ali',
#     'soyad':'Yılmaz',
#     'telefon':'532 000 00 01'
#  },
# '125':{
#     'ad':'Can',
#     'soyad':'Korkmaz',
#     'telefon':'532 000 00 02'   
#  },
# '128':{
#     'ad':'volkan',
#     'soyad':'Yükselen',
#     'telefon':'532 000 00 03'
#  },
# }
#1- bilgileri ver,len  öğrencileri kullanıcıdan aldığınız bilgilerle
#dictionary içinde saklayınız
#2-öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin

#1-
ogrenciler = {}
number = input("numara giriniz: ")
name = input("ad giriniz")
surname = input("soyad giriniz")
phone = input("telefon numarası giriniz")

# ogrenciler[number] = {
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone
# }
ogrenciler.update ({
number: {
    'ad':name,
     'soyad':surname,
     'telefon':phone
    }
})



number = input("numara giriniz: ")
name = input("ad giriniz")
surname = input("soyad giriniz")
phone = input("telefon numarası giriniz")

ogrenciler.update ({
number: {
    'ad':name,
     'soyad':surname,
     'telefon':phone
    }
})



number = input("numara giriniz: ")
name = input("ad giriniz")
surname = input("soyad giriniz")
phone = input("telefon numarası giriniz")

ogrenciler.update ({
number: {
    'ad':name,
     'soyad':surname,
     'telefon':phone
    }
})

print('*'*50)

ogrNo = input('ogrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"aradığınız {ogrNo} nolu öğrencinin adı {ogrenci['ad']} soyadı {ogrenci['soyad']} ve telefn numarası {ogrenci['telefon']} dur.")