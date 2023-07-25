# def greeting(name):
#     print('hello', name)

# print(greeting('ali'))
# print(greeting)

# sayHello =greeting
# print(sayHello)
# print(greeting)

# del sayHello
# print(sayHello)
# print(greeting)

# êncapsulation
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print('inner')
#         return num1 +1
#     num2 = inner_increment(num1)
#     print(num1, num2)
    
# outer(10)


def factorial(number):
    if not isinstance(number, int): #isinstance metodu number int türünde mi kontrol eder
        raise TypeError("number must be an integer")
    
    if not number >=0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)
try:
   print(factorial("4"))
except Exception as ex:
    print(ex)