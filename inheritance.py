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
#Child class will have access to parent class methods as well
c.m1() 
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

#Hierarchial Inheritance
class Parent:
    def m1(self):
        print('Single Parent class')

class Child1(Parent):
    def m2(self):
        print('child class 1')

class Child2(Parent):
    def m3(self):
        print('child class 2')

        
print('\n')
print('==='*15)
print('Hierarchial Inheritance')
print('==='*15)
c1 = Child1()
c1.m1()
c1.m2()
#c1.m3() # we get AttributeError: 'Child1' object has no attribute 'm3'; since method m3 belongs to child class 2 and actually not present in either of parent class and Child1 class.
c2 = Child2()
c2.m1()
#c2.m2() #AttributeError: 'Child2' object has no attribute 'm2'. Same as explained above
c2.m3()


#Diamond access problem in multiple inheritance
class Parent1:
    def m1(self):
        print('parent 1 method')
        
class Parent2:
    def m1(self):
        print('parent 2 method')
        
class Child(Parent1,Parent2):
    def m1(self):
        print('child method')

print('\n')
print('==='*15)
print('Diamond Access problem resolution')
print('Method exists in child class')
print('==='*15)       
c = Child()
c.m1() #child method

class Parent1:
    def m1(self):
        print('parent 1 method')
        
class Parent2:
    def m1(self):
        print('parent 2 method')
        
class Child(Parent1,Parent2):
    pass

print('\n')
print('==='*15)
print('Diamond Access problem resolution')
print('Method doent not exist in child class,depends on order of parent class')
print('==='*15) 
c = Child()
c.m1() #parent 1 method since its the first passed to the child class
#parent 2 method will get executed if its passed first
