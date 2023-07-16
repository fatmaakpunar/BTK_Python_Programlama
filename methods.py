#class
class Person: 
    # class attributes
    adress = 'no information'

    #constructor(yapıcı metod)
    def __init__(self, name, year):
        #object attributes

        self.name = name 
        self.year = year
       
       
     #instance methods
    def intro(self):
        print('Hello There I am ' + self.name)

    def calculateAge(self):
        return 2023 - self.year

#object (instance) 
p1 = Person(name ='fatma', year= 2015)
p2 = Person(name= 'merve', year=2012)

p1.intro()
p2.intro()

print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')