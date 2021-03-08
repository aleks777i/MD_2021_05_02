import random
import string


class Phone:
    def __init__(self, brand, os):
        self.brand = brand
        self.os = os
        self.number = "".join([random.choice(string.digits) for _ in range(11)])


Samsung = Phone("Samsung", "android")
print(Samsung.brand, Samsung.os, Samsung.number)
Apple = Phone("Apple", "ios")
print(Apple.brand, Apple.os, Apple.number)