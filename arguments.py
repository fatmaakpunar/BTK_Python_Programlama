# def changeName(n):
#     n = 'ada'
# name = 'Fatma'
# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'İstanbul'
# sehirler = ['Ankara', 'İzmir']
# change(sehirler)
# print(sehirler)

# def change(n): 
#     n[0] = 'istanbul'
# sehirler = ['ankara', 'izmir']
# n = sehirler[:]#slicing
# n[0] = 'istanbul'
# print(sehirler)
# print(n)

# def change(n):
#     n[0]='İstanbul'
# sehirler = ['Ankara', 'İzmir']
# change(sehirler[:])
# print(sehirler)

# def add(a, b,c=0):
#     return sum((a,b,c))
# print(add(10,20))
# print(add(10,20,30))

# def add(*params):
#     return sum((params))
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,50,63,23,56,14,25,89))

# def add (*params):
#     sum=0
#     for n in params:
#         sum = sum + n
#     return sum
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,50,63,23,56,14,25,89))

#parametrelerin veri sayısı ve tipi belli değil o zaman nasıl göndeririz?
def displayUser(**args):#dictionary için ** kullanırız tupple için * kullanırız
    for key, value in args.items():
        print('{} is {}'.format(key, value))
displayUser(name ='Fatma', age=22, city='İstanbul')
displayUser(name ='elif', age=13, city='Eskişehir', phone ='05** 365 2145')
displayUser(name ='yiğit', age=14, city='Ankara', phone ='05** 896 5321', email='yigit@gmail.com')

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myFunc(10,20,30,40,50, key1 = 'value 1',key2='value 2')
'''
çıktı=>
10 => a
20 => b
(30, 40, 50) => args
{'key1': 'value 1', 'key2': 'value 2'} => kwargs dictionary value
'''