import random
import string


class Phone:
    def __init__(self):
        self.number = "".join([random.choice(string.digits) for _ in range(11)])


class Samsung(Phone):
    def __init__(self):
        super().__init__()
        self.brand = "Samsung"
        self.os = "Android"


class Apple(Phone):
    def __init__(self):
        super().__init__()
        self.brand = "Apple"
        self.os = "ios"


iphone12 = Apple()
print(iphone12.brand, iphone12.os, iphone12.number)
s7 = Samsung()
print(s7.brand, s7.os, s7.number)

