def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ad = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ort= (not1 + not2 + not3)/3

    if 0<ort<35:
       harf ="FF"
    elif 35<=ort<40:
       harf ="DD"
    elif 40<=ort<50:
      harf ="DC"
    elif 50<=ort<60:
       harf ="CC"
    elif 60<=ort<65:
      harf ="CB"
    elif 65<=ort<70:
      harf ="BB"
    elif 70<=ort<80:
      harf ="BA"
    elif 80<=ort<=100:
      harf ="AA"
    else:
      pass
    return ad + ": " + harf + "\n"

def not_oku():
    with open("notlar.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input("isim: ")
    soyad =input("soyisim: ")
    not1 = int(input("not1: "))
    not2 = int(input("not2: "))
    not3 = int(input("not3: "))
    ort= (not1 + not2 + not3)/3
    with open("notlar.txt", "a", encoding="utf-8") as file:
      file.write(ad + " " + soyad + ": " + str(not1) + "," + str(not2) + "," + str(not3) + "\n") 

def kayit():
    with open("notlar.txt", "r",  encoding="utf-8") as file:
        liste = []
        for i in file:
           liste.append(not_hesapla(i))

        with open("kayit.txt", "w", encoding="utf-8") as file2:
           for i in liste:
                file2.write(i)

while True:
    islem = input("işleminizi seçiniz \n1-Notları oku \n2-Notları Gir \n3-Notları kayıt et \n4-Çıkış \n")
    if islem == '1':
        not_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        kayit()
    elif islem == '4':
        break