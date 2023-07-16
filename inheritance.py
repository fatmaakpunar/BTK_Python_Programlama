#Inheritance (Kalıtım): classların birbirinden miras alması

#Person => name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person)
#Person özellikleri miras yoluyla Student ve Teacher'a gidecek fakat Student veya Teacher'a eklenen bir özellik Person'ı etkilemiycek

#Animal=> Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('Person Created')
        
    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created')#Person Created
        
        #override
    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) #superde self'i göndermemize gerek yok
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = Person('Ali', 'Yılmaz')#Person Created
s1 = Student('Çınar', 'Turan', 1256)#Student Created
t1 = Teacher('Fatma', 'Akpunar', 'Math')

print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNumber))
print(t1.firstname + ' ' + t1.lastname + ' ' + t1.branch)

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
s1.sayHello()