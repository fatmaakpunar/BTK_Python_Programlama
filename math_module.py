#Yöntem 1
# import math
# import math as islem

# value = dir(math)
# value = help(math)
# value = help(math.factorial)

# value = math.sqrt(49)
# value =math.factorial(5)
# value = math.floor(5.9) #aşağı yuvarla
# value =math.ceil(5.9) #yukarı yuvarla

# value =islem.factorial(5)

#Yöntem 2
# from math import *


from math import factorial, sqrt

def sqrt(x):
    print("x: " + str(x)) #from math import factorial, sqrt geçersiz kılar

# value = factorial(5)
value =sqrt(9)

print(value)