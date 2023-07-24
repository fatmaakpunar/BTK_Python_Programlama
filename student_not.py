ad = str(input("isminiz: "))
soyad = str(input("soyisminiz: "))
vize = int(input("vize notunuzu giriniz: "))
final = int(input("final notunuzu giriniz: "))
ort = (vize*0.3) + (final*0.7)
if 0<ort<35:
   print("Notunuz FF")
   harf ="FF"
elif 35<=ort<40:
    print("Notunuz DD")
    harf ="DD"
elif 40<=ort<50:
   print("Notunuz DC")
   harf ="DC"
elif 50<=ort<60:
    print("Notunuz cc")
    harf ="CC"
elif 60<=ort<65:
    print("Notunuz CB")
    harf ="CB"
elif 65<=ort<70:
    print("Notunuz BB")
    harf ="BB"
elif 70<=ort<80:
    print("Notunuz BA")
    harf ="BA"
elif 80<=ort<=100:
    print("Notunuz AA")
    harf ="AA"
else:
   harf ="hatalı giriş"

with open("student.txt", "a", encoding="utf-8") as file:
     file.write(ad + " " + soyad + ": " + str(ort) + " " +  harf + "\n")
     