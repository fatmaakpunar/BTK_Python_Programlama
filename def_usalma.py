def usalma(number):
    def inner(power):
        return number ** power
    
    return inner

two = usalma(2)
three =usalma(3)
print(two(3))
print(three(4))