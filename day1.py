print("hello world")
if 5>2:
    print('5 is greater than 2')
x= 5
y='hello world'
print(x,y)

# python indentation

if 5>2:
    print("5 is greater")

# print without a new line
print('hello world', end=' ' )
print('my name is spandan')

print(3)
print(3*3)
print('i am',21,'years old')

# casting
x = str(2)
x = int(3)
x = float(3)

x=5
print(type(x))
a= 4
b =5
print(a+b)

a =4
b =5.6 
c = a+b
print(c)
print(type(c))

a = 'hello'
b= 'world'
c= a+b
print(c)
print(type(c))

a =4
b =2
c= a/b
print(c)
print(type(c))

name = input('enter name')
surname = input('enter surname')
fullname = (name + " " + surname)
print(fullname)

num1 = int(input('enter num1'))
num2 = int(input('enter num2'))
sum =num1+num2
print(sum)

name = input('enter name')
age = int(input('enter age'))
price =float(input( "enter price"))
print(name)
print(age)
print(price)

# indexing
a = 'spandan'
print(a[0])
print(a[5])
print(len(a)) 
# slicing
print(a[:8])

str ='hello worldlo'
str1=str.endswith('ld')
print(str1)
str2=str.capitalize()
print(str2)
str3 = str.count('lo')
print(str3)

a = int(input('enter num1'))
b = int(input('enter num2'))
if a<b:
    print("b is greater")
elif a==b:
    print('a and b are equal')
else:
    print('a is greater')

name = input('enter name')
age = int(input('enter age'))
if age>=18:
    if age<100:
        print(f'{name} can drive as he is {age} years old ')
    else:
        print("cannot drive")
else:
    print(f'{name} cannot drive')

