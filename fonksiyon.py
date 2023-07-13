# def sayHello(name = "user"): #define
#     print("Hello " + name)    
# sayHello("Fatma")
# sayHello()

def sayHello(name = 'user'):
    return 'Hello ' + name
msg=sayHello('Fatma')
print(msg)

def total(num1,num2):
    return num1+num2
result=total(20,10)
print(result)

def yasHesapla(dogumyili):
    return 2023-dogumyili
ageFatma =yasHesapla(2000)
print(ageFatma)

def emekliyekacyilkaldi(dogumyili, isim):
    '''
    DOCSTRİNG: Doğum yılınıza göre eömekliliğinize kaç yıl kaldı
    INPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    '''
    yas =yasHesapla(dogumyili)
    emeklilik = 65-yas
    if emeklilik>0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('zaten emekli oldunuz')
emekliyekacyilkaldi(2000, 'Fatma')

print(help(emekliyekacyilkaldi))