#class
class Person: #class ismi büyük harfle başlamalı, class dan sonra bir metod belirtmeliyiz
    # pass #yer tutucudur metod eklemezsek class hata vermez
    # class attributes
    adress = 'no information'
    #constructor(yapıcı metod)
    def __init__(self, name, year):#self p1 ve p2 yi temsil eder self olmak zorunda değil adı değiştirilebilir
        #object attributes
        self.name = name #p1 ya da p2 üzerine kullanıcının gönderdiği name bilgisi
        self.year = year
        print('init metodu çalıştı')
        #methods

#object (instance) obje küçük harfle başlamalı
p1 = Person(name ='fatma', year= 2015)
p2 = Person(name= 'merve', year=2012)

#updating
p1.name='ahmet'
p1.adress='istanbul'

#accessing object attributes
print(f'name: {p1.name} year: {p1.year} adress: {p1.adress}')
print(f'name: {p2.name} year: {p2.year} adress: {p2.adress}')

print(p1)
print(p2)