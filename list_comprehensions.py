#for ve while döngsüne alternatif bir yöntem
# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(numbers)

# numbers = [x for x in range(10)]
# print(numbers)


#x**2 için
# for x in range(10):
#     print(x**2)

# numbers = [x**2 for x in range(10)]
# print(numbers) 

#x*x lerden sadece 3' e bölünenleri yazdır
# numbers = [x*x for x in range(10) if x%3==0 ]
# print(numbers)


# myList = [] 
# myString = 'Hello'
# for letter in myString:
#     myList.append(letter)
# print(myList)

# myList=[letter for letter in myString]
# print(myList)

#yaş hesaplama
# years=[1983, 1999, 2008, 1956, 1986]
# ages = [2019-year for year in years]
# print(ages)

# result = [x if x%2==0 else 'TEK' for x in range(1,10)]
# print(result)

#iç-içe 2 döngümüz varsa
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)