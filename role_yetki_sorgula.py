def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolünün {1} sayfasına ulaşabilir.".format(role, page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
    return inner
user1 = yetki_sorgula("Product Edit")
print(user1('Admin'))
print(user1('User'))
