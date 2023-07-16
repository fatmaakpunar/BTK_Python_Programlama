class Circle:
    #class object attiruble
    pi=3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    #method
    def cevre_hesapla(self):
        return 2*self.pi + self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
    
c1=Circle() #yarıçap=1
c2=Circle(5)

print(f'c1: alan = {c1.alan_hesapla()} cevre = {c1.cevre_hesapla()}')
print(f'c1: alan = {c2.alan_hesapla()} cevre = {c2.cevre_hesapla()}')