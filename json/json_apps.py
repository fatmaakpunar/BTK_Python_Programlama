# Kullanıcıdan ailına username, password ve email bilgilerini users.json dosyasına kaydederek, 
# Login olma esnasından bu json dosyasından bilgileri çeker ve Login işlemini gerçekleştirir.

import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('user.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                  user =json.load(user)
                  newUser =User(username=user['username'], password= user['password'], email = user['email'])
                  self.users.append(newUser)
            print(self.users)
                    
       
    def register(self, user: User): #kullanıcı oluşturma işlemi
        self.users.append(user)
        self.savetoFile()
        print('kullanıcı oluşturuldu')

    def login(self,username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login Yapıldı')
                break

    def logout(self):
            self.isLoggedIn =False
            self.currentUser = {}
            print('çıkış yapıldı')

    def identity(self):
            if self.isLoggedIn:
                print(f'username: {self.currentUser.username}')
            else:
                print('giriş yapılamadı')

    def savetoFile(self):
        list =[]

        for user in self.users:
            list.append(json.dumps(user.__dict__)) #__dict__ verileri sözlük yapısına çevirir

        with open('users.json', 'w') as file:
            json.dump(list, file)

repository = UserRepository()

while True:
    print('Menü'.center(50,'*'))
    secim =input('1-Register\n2- Login\n3- Logout\n4- İdentity\n5- Exit\nseçiminiz: ')
    if secim =='5':
     break
    else:
        if secim=='1':
            #register
            username =input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username = username, password=password, email=email)
            repository.register(user)

        elif secim=='2':
            if repository.isLoggedIn:
                 print('zaten giriş yaptınız')
            else:
                username = input('username: ')
                password = input('password:' )
                repository.login(username, password)
        elif secim =='3':
            repository.logout()
        elif secim == '4':
            repository.identity()
        else:
            print("yanlış seçim")