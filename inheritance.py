#example code for different types of inheritance in Python

#Single Inheritance
class Parent:
    def m1(self):
        print('Parent class method')

class Child(Parent):
    def m2(self):
        print('child class method')

print('==='*15)
print('Single Inheritance')
print('==='*15)
c = Child()
c.m1() #can access parent class methods aswell
c.m2()


#Multi level Inheritance
class Grandfather:
    def m1(self):
        print('In Grandfather class')
        
class Father(Grandfather):
    def m2(self):
        print('In Father class')
        
class Son(Father):
    def m3(self):
        print('In Son class')

print('\n')
print('==='*15)
print('Multi level Inheritance')
print('==='*15)       
s = Son()
s.m1()
s.m2()
s.m3()
