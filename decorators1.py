def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önce işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper 

@my_decorator
def sayHello(name):
    print("hello", name)

sayHello("ali")