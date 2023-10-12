import random
i=0
puan =0
rakip =0
while i<3:
 
 rastgele = 0
 kullanici = int(input("1-Taş, 2-Kağıt, 3-Makas: "))
 rastgele = int(random.uniform(1, 3))

 if kullanici == 1:
    if rastgele == 1:
        print(rastgele, "taş")
    elif rastgele == 2:
        print(rastgele, "kağıt")
        rakip +=1
    elif rastgele == 3:
        print(rastgele, "makas")
        puan += 1
    
 elif kullanici ==2:
     if rastgele == 1:
        print(rastgele, "taş")
        puan += 1
     elif rastgele == 2:
        print(rastgele, "kağıt")
     elif rastgele == 3:
        print(rastgele, "makas")
        rakip +=1

 elif kullanici==3:
     if rastgele == 1:
        print(rastgele, "taş")
        rakip +=1
     elif rastgele == 2:
        print(rastgele, "kağıt")
        puan += 1
     elif rastgele == 3:
        print(rastgele, "makas")
        

 print(f'puanınız : {puan}')
 print(f'rakip puan: {rakip} ')
 i+=1
if puan>rakip:
 print("TEBRİKLER BÜYÜK KAZANAN SİZSİNİZ <3")
elif puan==rakip:
 print("BERABERE")
else:
 print("MALESEF RAKİBİNİZ KAZANDI :(")
 
 
