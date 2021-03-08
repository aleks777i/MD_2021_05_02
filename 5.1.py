import random
import string


class Phone:
    def __init__(self):
        self.number = "".join([random.choice(string.digits) for _ in range(11)])


class Samsung(Phone):
    brand = "Samsung"
    os = "Android"


class Apple(Phone):
    brand = "Apple"
    os = "ios"


iphone12 = Apple()
print(iphone12.brand, iphone12.os, iphone12.number)
s7 = Samsung()
print(s7.brand, s7.os, s7.number)
s9 = Samsung()
print(s9.brand, s9.number)



