# if,elif,else  

# tuple 


x = ["apple", "banana", "cherry"]
y = list(x)
print(y)
y.insert(0,"mango") 
x = tuple(y)
print(x) 



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 

a = ("apple", "banana", "cherry") 
b = list(a) 
print(b) 
b.append("orange" )
a = tuple(b) 
print(a) 

a = ("apple", "banana", "cherry","orange")
b = list(a)
b.remove("orange") 
a = tuple(b) 
print(a) 

#while loop

i = 2 
while i <= 100 : 
    print(i)
    i = i + 2 


# for loop     
fruits = ["apple", "banana", "cherry"] 
for fruit in fruits : 
    if fruit == "cherry" : 
        break
    print(fruit)
    print(len(fruit))


fruits = ["apple", "banana", "cherry"] 
for fruit in fruits : 
    if fruit == "apple" : 
        continue
    print(fruit)
    print(len(fruit)) 


for i in range(100) :
    if (i > 50) : 
        break
    print(i)


for i in range(1,100,3) :
    print(i)


# sort 

i = [2,6,7,9,23,54,1] 
i.sort(reverse=True) 
print(i)

# set union 

a = {1,2,3,4,3,6,7}
b = {11,12,13,14,13} 

print("union ", a | b)

# set intersection 

a = {1,2,3,4,3,6,7}
b = {11,12,13,14,13,3} 

print("union ", a & b)

#python dictionary 

dict = {'py':22,'hl':34,'rt':66,'op':56}
x = dict.keys()
print(x)

dict = {'py':22,'hl':34,'rt':66,'op':56}
x = dict.values()
print(x)

# dictionary update

dict = {'py':22,'hl':34,'rt':66,'op':56}
dict.update({'py': 24})
print(dict)

# dictionary addItem 

dict = {'py':22,'hl':34,'rt':66,'op':56}
dict['la'] = 88
print(dict)