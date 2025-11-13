list1 = [1,2,3,4,5,]
list2 = ['a','b','c','d','e']
list3 = list1 + list2
print(list3)

list1 = [1,2,3,4,5,6,7,8,9]
list1.append(10)
print(list1)

list1 =[8,5,8,9,4,3,2,6]
list1.sort()
print(list1)

list1 = [1,2,3,99,65,6,7,8,9]
# list1.sort(reverse=True) descending
# print(list1)

# list1.reverse() reverse
print(list1)

person = {
"name":"spandan",
"age": 21,
"sem":"seventh"
}
print(person)
print("the person age is",person['age'])

person['salary']= 60000
print(person)

del person['sem']
print(person)

family ={
    "child1":{
        "name": "ram"
    },
    "child2" : {
        "name": "hari"
    }
}
print(family)
 
i=1
while i<=20:
    if(i%2==0):
        print(i)
    i+=1

    