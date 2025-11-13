nep_currency = float(input('enter nepali currrency'))
usd = float(nep_currency /132)
print('the usd currency is',usd)

usd_currency = float(input('enter us currrency'))
nep = float(usd_currency * 132)
print('the nepali currency is',nep)


def nepali_to_usd(nepali_curr):
    usd= nepali_curr / 132
    return usd

def usd_to_nepali(us_curr):
    nep = us_curr *132
    return nep

print(nepali_to_usd(10000))

print(usd_to_nepali(10))

# factorial using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))

# fibonacci series using recursion
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    

print(fibonacci(5))

# recursion3
def showa(n):
    if n > 0:
        print(n)
        showa(n-1)

showa(5)

class Student:
    name="spandan"
# print(Student.name)

s1 = Student()
print(s1.name)
s2 = Student()
s2.name = "ram"
print(s2.name)
print(Student.name)

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f'{self.name} says woof') 
    def eat(self):
        print(f'{self.name} eats food')

dog1 = Dog('luffy','bhote')
print(dog1.name)
print(dog1.breed)
dog1.bark()
dog1.eat()

dog2 = Dog('kale','mix')
print(dog2.name)
print(dog2.breed)
dog2.bark()
dog2.eat()

class Calculator:
    def add(self,a,b):
        return a+b
    
calc = Calculator()
print(calc.add(5,4))

class Myclass:
    x=5
p1 = Myclass()
print(p1.x)
class person:
    def __init__(self,name,age):
        self.name =name
        self.age = age

p1 = person('spandan',21)
print(p1.name)
print(p1.age)
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

class Calculator:
    def add(self,a,b):
        return a+b
    
calc = Calculator()
print(calc.add(5,4))