import numpy as np
numbers1 = np.random.randint(10,100,6) #10 ile 100 arasında 6 tane rastgele sayı üretir
numbers2 = np.random.randint(10,100,6) #randint()yöntem, belirtilen aralıktan seçilen öğenin tamsayı değerini döndürür.
#print(numbers1)
#print(numbers2)

#result = numbers2 + numbers1   # iki dizinin elemanlarını toplar.
#result = numbers2 + 10    # dizinin elemanlarına 10 ekler.
#result = numbers2 - numbers1   # dizinin elemanlarını çıkartır.
#result = numbers1 * numbers2  # aynı indeksteki elemanları birbiri ile çarpılır.
# result = np.sin(numbers1)    # dizi elemanlarının sinüsünü alır.
# result = np.sqrt(numbers1)    # dizi elemanlarının karekökünü alır.
# result = np.log(numbers1)    # dizi elemanlarının logaritmasını alır.

mnumbers1 = numbers1.reshape(2,3) #6 elemanlı diziyi 2 satır 3 sütunluk matris yapıyoruz.
mnumbers2 = numbers2.reshape(2,3)



#result =np.vstack((mnumbers1, mnumbers2)) # iki matrisi dikey (horizontal) olarak birleştirir.
#result = np.hstack((mnumbers1, mnumbers2))# iki matrisi yatay (vertical) olarak birleştirir.
result = numbers1 >= 50   # matrisin elemanlarının 50 den büyük olup olmadığını kontrol eder ve True/False olarak yanıt verir. 
result = numbers2 % 2 == 0# matrisin elemanlarının çift olup olmadığını kontrol eder ve True/False olarak yanıt verir. 
print(mnumbers1)
print(mnumbers2)
print("*************")
print(numbers2[result])     # çift olan sayıları numbers2 değişkenine atar ve ekrana yazdırır.  result True olan indeksleri seçer.


#print(result)