#map dizinin elemanlarını tek tek fonksiyona gönderir
# def square(num): return num**2
# numbers=[1,3,5,9]
# result =list(map(square, numbers))
# for item in map(square, numbers):
#     print(item)
# print(result)

#isimsiz fonksiyon
# numbers=[1,3,5,9]
# result =list(map(lambda num: num**2, numbers))
# print(result)

#FİLTER
numbers=[1,3,5,9,10,4]
def check_even(num): return num%2==0
result= list(filter(check_even, numbers))
print(result)