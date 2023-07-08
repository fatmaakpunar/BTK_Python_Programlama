numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']
# val = min(numbers)
# val = max(numbers)
# val = min(letters)
# val = max(letters)
# val = numbers[3:6]
# val = numbers[:3]
# numbers[4] = 40
# print(numbers)
 #UYGULAMA
names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000 ,1998, 1987]

#1-'Cenk' ismini listenin sonuna ekleyiniz
# names.append('Cenk')
# print(names)

#2-'Sena' değerini listenin başına ekleyiniz
# names.insert(0,'sena')
# print(names)

#3-'Deniz' ismini listeden siliniz
# names.pop()
# print(names)

#4-'Deniz' isminin indeksi nedir?
# index = names.index('Deniz')
# print(index)

#5-ali listenin bir elemanı mıdır?
# result = 'Ali' in names
# print(result)

#6-kullanıcıdan alıcağınız 3 marka ismini bir listede saklayınız.
markalar = []
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
print(markalar)