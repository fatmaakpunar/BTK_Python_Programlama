#index numaralarını daha kolay oluşturmayı sağlar
# index=0
# greeting ='hello there'
# for letter in greeting:
#     print(f'letter: {letter} index: {index}')
#     index +=1

greeting = 'Hello'
for index, item in enumerate(greeting):
    print(f'index: {index} letter: {item}')