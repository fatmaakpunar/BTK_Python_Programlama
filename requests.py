#bilgisayarımıza python kurulumuyla gelmez
#https://pypi.org/project/selenium-requests/ sayfasında bu modülle ilgili detaylı bilgi var
#terminale pip install requests komutuyla modülü yükledik
#html kodlarına ulaşırız
import requests
import json 

result = requests.get("https://jsonplaceholder.typicode.com/todos") #çıktının 200 olması her şey yolunda demektir
result = json.loads(result.text)
for i in result:
    if i["userId"] == 1:
        if i["title"] == 1:
            print(i["title"])

print(type(result))