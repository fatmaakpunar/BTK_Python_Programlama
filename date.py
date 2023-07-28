from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time
# import datetime
simdi= datetime.now() #"now" yerine "today" de diyebiliriz.
result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second
result = datetime.ctime(simdi)#daha açıklayıcı bir bilgi verir
result = datetime.strftime(simdi, '%Y') #yıl
result = datetime.strftime(simdi, '%X') #saat
result = datetime.strftime(simdi, '%d') #gün
result = datetime.strftime(simdi, '%A') #gün isim olarak friday
result = datetime.strftime(simdi, '%B') #ay isim olarak july
result = datetime.strftime(simdi, '%Y %B %A') #2023 July Friday
#peki bu bilgilere nasıl ulaşıcaz x in saat olduğunu nasıl bilicez 
#google=> datetimepython => w3scholls.com

# t= '28 Temmuz 2023'
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

t='15 April 2019 hour  10:12:30'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

birthday =datetime(2011,8,12,8,6,45)
result=datetime.timestamp(birthday)# saniye
result=datetime.fromtimestamp(result)#saniye to datetime
result=datetime.fromtimestamp(0)
result=simdi-birthday#timedelta
# result=result.days# timedelta gün bilgisi
# result=result.seconds
# result=result.microseconds

result=simdi+timedelta(days=10)
print(simdi)

print(result)