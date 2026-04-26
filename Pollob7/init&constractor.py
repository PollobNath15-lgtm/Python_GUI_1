class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Name:{self.name}\nage:{self.age} ")

p1=Person("jj",32)

p1.greet()