# #global scope
# x= 'global x'
# def function():
#     #local scope
#     x='local x'
# function()
# print(x)

# #global
# name = 'Fatma'
# def changeName(new_name):
#     #local
#     name=new_name
#     print(name)
# changeName('Akpunar')
# print(name)

# name ='global  string'
# def greeting():
#     name='Fatma'

#     def hello():
#         print('hello '+name)
#     hello()
# greeting()

x=50
def test():
    global x #bunu tanımlarsak globali alır
    print(f'x : {x}')
    x=100
    print(f'changed x to {x}')
test()
print(x)