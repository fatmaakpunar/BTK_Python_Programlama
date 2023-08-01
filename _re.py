import re
result = dir(re)

#re modülü
str = "Python kursu: Python Programlama Rehberiniz | 40 saat"
#re.findal()
# result = re.findall("Python",str)
# result = len(result)

#re.split()
# result = re.split(" ",str)

 #re.sub()
# result = re.sub(" ","-",str) #boşluk karakterini - çevirir boşluk yerine"\s" de yazılabilir

#re.search()
# result = re.search("Python",str) #str içinde pythonu arar ve konumunu verir
# result = result.span() #konum verir
# result = result.start() #konumun başladığı yer
# result = result.end() #konumun bittiği yer
# result = result.group() #bulduğu ifadeyi geri gönderir
# result = result.string #aradığı ifadeyi nerede aradığını yazdırır

"""
[] - Köşeli parantezler arasına yazılan bütün karakterler aranır.
[abc] => a : 1 match
         ac : 2 match
         Python No matches

[a-e] => [abcde]
[1-5] => [12345]
[0-39] => [01239]

[^abc] => abc dışındaki karakterler.
[^0-9] => rakam olmayan karakterler.

"""
result = re.findall("[abc]", str) #a,b,c
result = re.findall("[sat]", str) #s,a,t
result = re.findall("[a-e]", str) #a,b,c,d,e
result = re.findall("[a-z]", str) #a dan z ye tüm karakterler
result = re.findall("[0-5]", str) #0,1,2,3,4,5
result = re.findall("[^abc]", str) #a,b,c hariç tüm karakterler
result = re.findall ("[^0-9]", str) #0-9 arakamlar hariç tüm karakterler

"""
. => Her hangi bir tek karateri belirtir
.. => a    :  No match
      ab   :  1 match
      abc  :  1 match ab değeri döner
      abcd :  2 matches ab ve cd şeklinde geri döner
"""
result = re.findall("...",str)
result =re.findall("Py..on",str)

"""
^ - Belirtilen karakterlerle başlıyor mu?
^a => a: 1 match
      abc: 1 match
      bac: No match
"""
result = re.findall("^P",str)

"""
$ - belirtilen karakterle bitiyor mu?
a$ => a      :  1 match
      lamba  :  1 match
      Python :  No match
"""
result = re.findall("t$",str)
result =re.findall("saat$",str)

"""
* - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
ma*n=> mn : 1 match
       man : 1 match
       maaan : 1 match
       main : No match (a' nın arkasına n gelmiyor.)
"""
result =re.findall("sa*t",str)

"""
+ - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
ma+n => mn : No match
        man: 1 match
        maaan : 1 match
       main: No match (a nın arkasına n gelmiyor.)
"""
result = re.findall("sa+t", str)

"""
?- Bir karakterin sıfır ya da bir kez olmasını kontrol eder.
ma+n => mn   : No match
        man  : 1 match
        maaan: 1 match
        main : No match (a' nın arkasına n gelmiyor.)
"""
result =re.findall("sa?t",str)

"""
{} - Karakter sayısını kontrol eder.

     a1{2} => a karakterinin arkasına 1 karakteri 2 kez tekrarlamalı.
     al{2,3}=> a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlanmalı.
     [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result = re.findall("a{2}",str)

"""
|- alternatif seçeneklerden birinin gerçekleşmesi gerekir.
a|b => a ya da b

     cde => no match
     ade => 1 match
     acdbea => 3 match
"""

"""
() - gruplamak için kullanılır.
(a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

"""
\ - Özel karakterleri aramamızı sağlar.
\$a => $ karakterinin arkasına a karakterinin arar. Yani 
       $ regular exp. engine tarafından yorumlanmaz.

\A - Belirtilen karakter string in başında mı ?
     \Athe=> the string in başındamı

     result = re.findall("\APython", str)
     result = re.findall("saat\Z", str)

\Z - Belirtilen karakter string in sonunda mı ? 
     the\Z => the string in sonunda mı

\b - Belirtilen karakter kelimenin in başında ya da sonunda mı ? 
     \bthe => the kelimenin in başında mı?

\B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ? 
     \Bthe => the kelimenin in başında değil mi? 
     the\B => the kelimenin in sonunda değil mi? 

\d - [0-9] ile aynı anlama gelir yani rakamları arar. 
     \d => 12abc34

\D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
     \D => 1ab44_50


     \s - Boşluk karakterlerini arar.
     \S - Boşluk karakterleri dışındakiler. 
     \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri. 
     \พ - \w nin tam tersi
"""

print(result)