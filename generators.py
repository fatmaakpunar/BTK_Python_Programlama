#bellekte yer işgal etmeyen bir iterator üretir
# def cube():
#     result = []

#     for i in range(500000):
#         result.append(i**3)
#     return result

# print(cube())


# def cube():
#     for i in range(5):
#         yield i**3 #eğer bir fonksiyon yield ifadesi içeriyorsa bir generator fonksiyonu haline dönüşür
# generator = cube()
# iterator=iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# def cube():
#     for i in range(5):
#         yield i**3
# iterator = cube()

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# def cube():
#     for i in range(5):
#         yield i**3

# for i in cube():
#     print(i)

generator= (i**3 for i in range(5))
print(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))