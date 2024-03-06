from datetime import datetime
class Person(object):
    def __init__(self, name, country, birthyear):
        self.name = name
        self.country = country
        self.birthyear = birthyear
    
    def age(self):
        return abs(self.birthyear - datetime.now().year)
obj = Person("Tom", "India", 2002)
print(obj.age())

