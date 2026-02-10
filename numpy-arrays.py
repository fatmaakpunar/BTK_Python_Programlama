import numpy as np

#result = np.array([1,3,5,7,9])
#result = np.arange(1,10)
#result = np.arange(10,100,3) # 10 dan 100 e kadar üçer üçer
#result = np.zeros(10) #10 tane 0
#result =np.ones(10) # 10 tane 1
#result = np.linspace(0,100,5) # 5 parçaya böler aralığı
#result = np.linspace(0,5,5)
#result = np.random.randint(0,10) # 0 ile 10 arası rastgele sayı üretir
#result = np.random.randint(20) #başlangıcı 0 dan alır
#result = np.random.rand(5) # 0 ile 1 arası 5 sayı üretir
#result = np.arange(50) # 0,49 arası sayıları getirir
#np_array = np.arange(50)
#np_multi = np_array.reshape(5,10) # 5,10 matris
#print(np_multi.sum(axis=1)) # satırların toplamı
#print(np_multi.sum(axis=0)) #sütunların toplamı
rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
#result = rnd_numbers.max()
#result = rnd_numbers.min()
#result = rnd_numbers.mean()
#result = rnd_numbers.argmin()
result = rnd_numbers.argmax()

print(result)