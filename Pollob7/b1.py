class A:
    def add(self ,a,b):
        return a+b
class B:
    def sub(self,a,b):
        return a-b
class C:
    pass

x=A()
y=B()

print(x.add(4,6))
print(y.sub(5,7))