def islem(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
         toplam = toplam+i
        return toplam
        
    def carpma(*args):
       carpim = 1
       for i in args:
        carpim = carpim*i
       return carpim
    
    if islem_adi == "toplama":
       return toplama
    else:
       return carpma
    
toplama = islem("toplama")
print(toplama(3,5,6,7))

carpma = islem("carpma")
print(carpma(1, 2, 3, 6, 4))