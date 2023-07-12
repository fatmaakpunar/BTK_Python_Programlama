
#Soru: Girilen bir sayının asal olup olmadığını bulun.

sayi = int(input('sayı: '))
asalmi=True
if sayi == 1:
    print('1 sayısı asal değildir')
for i in range(2,sayi):
    if (sayi%i==0):
        asalmi=False
        break
if asalmi:
    print('sayı asaldır')
else:
    print('sayı asal değil')