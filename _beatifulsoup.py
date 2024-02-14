html_doc ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam değil :| </title>
</head>
<body>
<h1 id = "header">
        FATMA AKPUNAR
    </h1>
    <div class="grup1">
        <h2>
        Programlama
        </h2>

        <ul>
            <li>MENÜ 1</li>
            <li>MENÜ 2</li>
            <li>MENÜ 3</li>
        </ul>

   </div>
   <div class="grup2">
    <h2>
        Modüller
    </h2>
    <ul>
        <li>MENÜ 1</li>
        <li>MENÜ 2</li>
        <li>MENÜ 3</li>
    </ul>
   </div>

    
</body>
</html>
"""
from bs4 import BeautifulSoup

soup =BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify() #belgeyi daha okunabilir bir şekilde düzenleyerek dize olarak döndürür
result = soup.title #title içeriği gelir
result = soup.head
result = soup.body

result = soup.title.name #title ismi gelir
result = soup.titleistring #içindeki string bilgisi gelir

result = soup.h2 #ilk h2'yi getirir

result = soup.find_all('h2') #bütün h2'leri getiri
result = soup.find_all('h2')[0] #ilk h2'yi getirir

result = soup.find_all('div')[1].ul.find_all('li') #bu şekilde de kullanılabilir

result = soup.findChildren('div') #div'in altındaki tüm etiketleri getirir


print(result)