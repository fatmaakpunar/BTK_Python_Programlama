import random 
result =dir(random)

# result=random.random() #0.0 ile 1.0 arasında sayı üretir
result=random.random()*100 #0.0 ile 100.0 arası sayı üretir
result=random.uniform(1, 10) #1 ile 10 arası ondalıklı sayı üretir
result=int(random.uniform(1, 10))# sayıların tam kısmını bize verir
result = random.randint(1,100) #1 ile 100 arası tam sayı üretir
greeting='Hello There'
names = ['ali', 'yağmur', 'deniz', 'cenk', 'ahmet', 'efe']
# result = names[random.randint(0,len(names)-1)]
result=random.choice(names)#liste içinden rastgele eleman seçer
result=random.choice(greeting)#'Hello There' her bir karakterini rastgele olarak getirir

liste=list(range(10))
random.shuffle(liste)#elemanlar random olarak sıralanmış gelir
result=liste

liste=range(100)
result=random.sample(liste, 3)#listenin içinden 3 tane rastgele sayı getir
result=random.sample(names, 2)

print(result)