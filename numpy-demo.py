import numpy as np
#result = np.array([10,15,30,45,60]) #1

#result = np.arange(5,15) #2

#result = np.arange(50,100,5) #3

#result = np.zeros(10) #4

#result = np.ones(10) #5

#6 (0-100) arasında eşit aralıklı 5 sayı üret
#result = np.linspace(0,100,5) 

#7 (10,30) arasında rasgele 5 tamsayı üret
#result = np.random.randint(10,30,5) 

#8 [-1 ile 1] arasında 10 adet sayı üretin
#result = np.random.uniform(-1,1,10) 

#9. soru (3x5) boyutlarında (10-50) arasında rasgele bir matris oluştur
# result = np.random.randint(10,50,15)
# matris = result.reshape(3,5)
#print(result)
# print("************")
# print(matris)
# print("************")

# #10.soru satır sütun toplamı üretilen matrisin
# print(matris.sum(axis=1)) #satır
# print(matris.sum(axis=0))#sütun
# print("************")

# #11. soru 
# resultmax = matris.max()
# resultmin = matris.min()
# resultmean = matris.mean()
# print("************")
# print(resultmax)
# print(resultmin)
# print(resultmean)

# #12. soru üretilen matrisin en büyük değerinin indeksi nedir
# print("************")
# resultmaxindex = matris.argmax()   
# resultminindex = matris.argmin()
# print(resultmaxindex)
# print(resultminindex)

#13 dizinin ilk 3 elemanını yazdırma
# result = np.arange(10,20)
# dizi = result[0:3]

# #14 dizinin elemanlarını tersten yazdırma
# diziters = result[::-1]
# print(diziters)

#15 matrisin ilk satırını seç
# print(matris)
# print("************")
# print(matris[0])

#16 üretilen matrisin 2. satır 3. sütundaki elemanı
#print(matris[1][2])

#17 üretilen matrisin tüm satırlardaki ilk elemanı 
#print(matris[:,0])

#18 üretilem matrisin her bir elemanının karesi
#print(matris**2)

#19 üretilen matris elemanlarının hangisi pozitif çift sayıdır?
# result = np.arange(-50,50)
# print(result)
# print("************")
# number = result % 2 == 0
# number = result > 0
# print(result[number]) 