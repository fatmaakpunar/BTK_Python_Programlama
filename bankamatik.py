#Bankamatik Uygulaması
FatmaHesap = {
  'ad':'Fatma Akpunar',
  'hesapno': '1357911',
  'bakiye':3000,
  'ekhesap':2000
 }

MerveHesap = {
  'ad':'Merve Akpunar',
  'hesapno': '246810',
  'bakiye':2000,
  'ekhesap':1000
 }

def paracek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye']>=miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']

        if (toplam>=miktar):
            ekhesapkullanimi = input('ek hesap kullanılsın mı? (e/h)')
            if ekhesapkullanimi =='e':
                ekhesapkullanilacakmiktar =miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekhesap']-= ekhesapkullanilacakmiktar
                print('paranızı alabilirsiniz')
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print('üzgünüz bakiye yetersiz')

def bakiyesorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekhesap']} TL bulunmaktadır.")
paracek(FatmaHesap,3000)
bakiyesorgula(FatmaHesap)
print('*********************************')
paracek(FatmaHesap,2000)
bakiyesorgula(FatmaHesap)