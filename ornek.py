from operator import length_hint


website="http://www.sadikturan.com"
course="Python Kursu:Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1- 'course' karakter dizisinde kaç karakter bulunmalıdır ?
result=len(course)
print(result)
#'website' içinden www karakterlerini alın
print(website[7:10])
#'course' içinden ilk 15 ve son 15 karakterlerini alın
print(course[:15])
print(course[-15:])
#'course' ifadesindeki karakterleri tersten yazdıralım
print(course[::-1])
s="Hello world"
s=s[0:6] + 'W' +s[-4:]
print(s)

