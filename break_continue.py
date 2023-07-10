
#m görünce dursun
# name = 'Fatma Akpunar'
# for letter in name:
#    if letter == 'm':
#     break
#    print(letter)

#sadece m yi çıkarsın
# name = 'Fatma Akpunar'
# for letter in name:
#    if letter == 'm':
#     continue
#    print(letter)

# x=0
# while x<5:
#     if x== 2:
#         continue
#     print(x)
#     x+=1

#1- 1 den 100 ekadar tek sayıların toplamı
x=1
result=0
while x<=100:
    x+=1
    if x%2==1:
        continue
    result+=x
    
print(f'toplam: {result}')
    
