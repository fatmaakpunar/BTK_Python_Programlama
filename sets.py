fruits = {'orange', 'apple', 'banana'}
# print(fruits[0]) indekslenemez 
#elemanları döngü kullanarak bulabiliriz

for x in fruits:
    print(x)

    fruits.add('cherry')
    fruits.update(['mango', 'grape'])
    fruits.remove('mango')
    fruits.discard('apple')
    print(fruits)